# human parsing datasets analysis

In this repo I want to examin some of datasets that use in human parsing task.

- for more information about human parsinag task please see [Human Parsing](https://paperswithcode.com/task/human-parsing/latest)

# Lsit of datasets:
- CIHP
- LIP

## LIP
**LIP** is a single human parsing datasets
for download ad prepare dataset run:
```
cd /YOUR/TARGET/PATH
wget https://raw.githubusercontent.com/msinamsina/human-parsing-datasets-analysis/main/src/lip/prepare_LIP.sh
./prepare_LIP.sh
```

## CIHP:
**instance level human parsing** dataset or **CIHP** is one of datasets that use in human parsing task.

for download use this [google drive](https://drive.google.com/drive/folders/0BzvH3bSnp3E9ZW9paE9kdkJtM3M?resourcekey=0-vgKJX42GVFaAwjhEWAncjQ)
Or run :
```
gdown 1HdqA8yWVxZ8od0hngKzZTziHx_ONzCWj
tar -xvf  instance-level_human_parsing.tar.gz
mv instance-level_human_parsing datasets/CIHP

```
This dataset has 19 classes consists of:
1. Hat: Hat, helmet, cap, hood, veil, headscarf, part covering the skull and hair of a hood/balaclava, crown…
2. Hair
3. Glove
4. Sunglasses/Glasses: Sunglasses, eyewear, protective glasses…
5. UpperClothes: T-shirt, shirt, tank top, sweater under a coat, top of a dress…
6. Face Mask: Protective mask, surgical mask, carnival mask, facial part of a balaclava, visor of a helmet…
7. Coat: Coat, jacket worn without anything on it, vest with nothing on it, a sweater with nothing on it…
8. Socks
9. Pants: Pants, shorts, tights, leggings, swimsuit bottoms… (clothing with 2 legs)
10. Torso-skin
11. Scarf: Scarf, bow tie, tie…
12. Skirt: Skirt, kilt, bottom of a dress…
13. Face
14. Left-arm (naked part)
15. Right-arm (naked part)
16. Left-leg (naked part)
17. Right-leg (naked part)
18. Left-shoe
19. Right-shoe

## All objects instances are listed below

### train set

|  category  | #instances   |  category  | #instances   |   category   | #instances   | 
|:----------:|:-------------|:----------:|:-------------|:------------:|:-------------|
|   Person   | 93209        |    Hat     | 14407        |     Hair     | 83797        |
|   Glove    | 3245         | Sunglasses | 3550         | UpperClothes | 72028        |
|   Dress    | 7777         |    Coat    | 32675        |    Socks     | 6283         |
|   Pants    | 50798        | Torso-skin | 77807        |    Scarf     | 2985         |
|   Skirt    | 3301         |    Face    | 87961        |   Left-arm   | 59088        |
| Right-arm  | 61425        |  Left-leg  | 15038        |  Right-leg   | 14963        |
| Left-shoe  | 24799        | Right-shoe | 24809        |              |              |
|   total    | 739945       |            |              |              |              |


### validation set
|  category  | #instances   |  category  | #instances   |   category   | #instances   |
|:----------:|:-------------|:----------:|:-------------|:------------:|:-------------|
|   Person   | 17520        |    Hat     | 2536         |     Hair     | 15797        |
|   Glove    | 530          | Sunglasses | 697          | UpperClothes | 13497        |
|   Dress    | 1509         |    Coat    | 6055         |    Socks     | 1109         |
|   Pants    | 9624         | Torso-skin | 14383        |    Scarf     | 575          |
|   Skirt    | 578          |    Face    | 16489        |   Left-arm   | 11249        |
| Right-arm  | 11825        |  Left-leg  | 2815         |  Right-leg   | 2809         |
| Left-shoe  | 4622         | Right-shoe | 4618         |              |              |
|   total    | 138837       |            |              |              |              |

### pixel density for train set
|  category  | #pixel      |  category  | #pixel      |   category   | #pixel      |
|:----------:|:------------|:----------:|:------------|:------------:|:------------|
|   bg       | 2.98476e+09 |    Hat     | 3.16891e+07 |     Hair     | 2.3207e+08  |
|   Glove    | 3.09781e+06 | Sunglasses | 2.00425e+06 | UpperClothes | 4.79024e+08 |
|   Dress    | 1.00995e+08 |    Coat    | 3.69077e+08 |    Socks     | 6.47901e+06 |
|   Pants    | 2.02236e+08 | Torso-skin | 7.33666e+07 |    Scarf     | 9.95388e+06 |
|   Skirt    | 1.79153e+07 |    Face    | 2.21155e+08 |   Left-arm   | 7.85701e+07 |
| Right-arm  | 8.40876e+07 |  Left-leg  | 1.88156e+07 |  Right-leg   | 1.86267e+07 |
| Left-shoe  | 1.09868e+07 | Right-shoe | 1.11426e+07 |              |             |

### pixel density for validation set

|  category  | #pixel      |  category  | #pixel      |   category   | #pixel      |
|:----------:|:------------|:----------:|:------------|:------------:|:------------|
|   bg   | 5.33618e+08 |    Hat     | 5.56226e+06 |     Hair     | 4.07608e+07 |
|   Glove    | 522334      | Sunglasses | 379419      | UpperClothes | 8.48936e+07 |
|   Dress    | 1.73518e+07 |    Coat    | 6.33057e+07 |    Socks     | 1.28626e+06 |
|   Pants    | 3.57697e+07 | Torso-skin | 1.23061e+07 |    Scarf     | 1.91357e+06 |
|   Skirt    | 2.93269e+06 |    Face    | 3.79325e+07 |   Left-arm   | 1.32471e+07 |
| Right-arm  | 1.46803e+07 |  Left-leg  | 3.13814e+06 |  Right-leg   | 3.10248e+06 |
| Left-shoe  | 1.96614e+06 | Right-shoe | 1.99029e+06 |              |             |


