gdown 1pK-jTsD1COp5tVBDmi27ijDPyxmXncZB
unzip LIP.zip
cd LIP
unzip Testing_images.zip
unzip Train_parsing_reversed_labels.zip
unzip TrainVal_images.zip
unzip TrainVal_images.zip
unzip TrainVal_parsing_annotations.zip
unzip TrainVal_pose_annotations.zip
rm *.zip
mv /content/Self-Correction-Human-Parsing/data/LIP/TrainVal_parsing_annotations/TrainVal_parsing_annotations.zip ./
unzip TrainVal_parsing_annotations.zip
rm *.zip