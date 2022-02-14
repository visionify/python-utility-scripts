import glob
import os
import numpy as np
import shutil
import random

# Change for different dataset
data_path = '/home/digvijay-jetxavier/pytorch-ssd/data/shelf-detection-augmentations/'

shelf_jpgs = glob.glob(data_path + '*.jpg')
shelf_xml = glob.glob(data_path + '*.xml')


#SANITY CHECK
# print(shelf_jpgs)
# print(shelf_xml)

if not os.path.exists(data_path + 'JPEGImages/'):
    os.makedirs(data_path + 'JPEGImages/')
if not os.path.exists(data_path + 'Annotations/'):
    os.makedirs(data_path + 'Annotations/')
if not os.path.exists(data_path + 'ImageSets/Main/'):
    os.makedirs(data_path + 'ImageSets/Main/')

for imgs in shelf_jpgs:
    shutil.move(imgs, data_path + 'JPEGImages/')

for xmls in shelf_xml:
    shutil.move(xmls, data_path + 'Annotations/')

## Generate a txt file for ImageSets
a = open(data_path + 'ImageSets/Main/train.txt', "w+")
for file in glob.glob(data_path + 'Annotations/*.xml'):
    # print(file)
    f = file.rstrip('*.xml').split('/')[-1]
    # print(f)
    a.write(str(f) + os.linesep)

##push all names to array
## random splitting
