# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
"""
Detection Training Script.

This scripts reads a given config file and runs the training or evaluation.
It is an entry point that is made to train standard models in detectron2.

In order to let one script support training of many models,
this script contains logic that are specific to these built-in models and therefore
may not be suitable for your own project.
For example, your research project perhaps only needs a single "evaluator".

Therefore, we recommend you to use detectron2 as an library and take
this file as an example of how to use the library.
You may want to write your own script with your datasets and other customizations.
"""
from adet.data import datasets
import detectron2.utils.comm as comm
from detectron2.data import MetadataCatalog, build_detection_train_loader, build_detection_test_loader
from detectron2.engine import DefaultPredictor, default_argument_parser, default_setup, hooks, launch
from detectron2.utils.logger import setup_logger

from adet.config import get_cfg
from detectron2.data import DatasetCatalog, MetadataCatalog
from detectron2.data.dataset_mapper import DatasetMapper
from detectron2.data.samplers import (
    InferenceSampler,
)
import logging
from detectron2.utils.logger import _log_api_usage, log_first_n
from tabulate import tabulate
from termcolor import colored
import itertools
import torch
import numpy as np


class parsing_dataset_analyser:
    @classmethod
    def get_data_set(cls, cfg):
        dataset_name = cfg.DATASETS.TEST[0]
        dataset_dicts = DatasetCatalog.get(dataset_name)
        metadata = MetadataCatalog.get(dataset_name)
        return dataset_dicts, metadata

    @classmethod
    def build_train_loader(cls, cfg):
        return build_detection_train_loader(cfg,
                                            mapper=DatasetMapper(cfg, True, augmentations=[]),
                                            sampler=InferenceSampler(len(DatasetCatalog.get(cfg.DATASETS.TRAIN[0]))))

    @classmethod
    def build_test_loader(cls, cfg, dataset_name):
        return build_detection_test_loader(cfg, dataset_name,
                                           mapper=DatasetMapper(cfg, True, augmentations=[]),
                                           sampler=InferenceSampler(len(DatasetCatalog.get(cfg.DATASETS.TEST[0]))))


def setup(args):
    """
    Create configs and perform basic setups.
    """
    cfg = get_cfg()
    cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(args.opts)
    cfg.freeze()
    default_setup(cfg, args)

    rank = comm.get_rank()
    setup_logger(cfg.OUTPUT_DIR, distributed_rank=rank, name="adet")

    return cfg


def main(args):
    cfg = setup(args)
    datasets, metadata = parsing_dataset_analyser.get_data_set(cfg)
    if args.eval_only:
        dataloader = parsing_dataset_analyser.build_test_loader(cfg, cfg.DATASETS.TEST[0])
    else:
        dataloader = parsing_dataset_analyser.build_train_loader(cfg)
    with torch.no_grad():
        # data = next(iter(dataloader))
        # tmp = (data[0]['sem_seg'].detach().view(-1).bincount(
        #     minlength=cfg.MODEL.SEM_SEG_HEAD.NUM_CLASSES).numpy())
        logger = logging.getLogger("adet")
        tmp = np.zeros(cfg.MODEL.SEM_SEG_HEAD.NUM_CLASSES)
        for i, data in enumerate(dataloader):
            tmp += (data[0]['sem_seg'].detach().view(-1).bincount(
                minlength=cfg.MODEL.SEM_SEG_HEAD.NUM_CLASSES).detach().numpy())

            if i % 100 == 0:
                string = f'{i}\n'
                string += ''.join([ f'| {metadata.get("thing_classes")[i]} | {tmp[i]} |' for i in range(len(tmp))] )
                logger.info(string)

    data = list(
        itertools.chain(
            *[[metadata.get("thing_classes")[i], tmp[i].item()] for i in range(len(metadata.get("thing_classes")))])
    )
    data = itertools.zip_longest(*[data[i::6] for i in range(6)])

    table = tabulate(
        data,
        headers=["category", "#pixel"] * (6 // 2),
        tablefmt="pipe",
        numalign="left",
        stralign="center",
    )
    log_first_n(
        logging.INFO,
        "Distribution of instances among all :\n"
        + colored(table, "cyan"),
        key="message",
    )

    return None


if __name__ == "__main__":
    args = default_argument_parser().parse_args()
    print("Command Line Args:", args)
    launch(
        main,
        args.num_gpus,
        num_machines=args.num_machines,
        machine_rank=args.machine_rank,
        dist_url=args.dist_url,
        args=(args,),
    )
