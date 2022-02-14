import numpy as np
from random import shuffle
import os
import math
import glob
import random
import shutil

data_path = '/home/digvijay-jetxavier/pytorch-ssd/data/shelf-detection-images/'

all_images = glob.glob(os.path.join(data_path, 'JPEGImages/*.jpg'))


# print(all_images) SANITY CHECK

train_pct = 0.4
trainval_pct = 0.3
val_pct = 0.2
test_pct = 0.1

total_imgs = len(all_images)
train_imgs = math.floor(total_imgs*train_pct)
val_imgs = math.floor(total_imgs*val_pct) 
trainval_imgs = math.floor(total_imgs*trainval_pct) 
test_imgs = math.floor(total_imgs*test_pct) 

# print(train_imgs, trainval_imgs, val_imgs, test_imgs) SANITY CHECKS


a = open(data_path + 'ImageSets/Main/train.txt', "w+")
b = open(data_path + 'ImageSets/Main/trainval.txt', "w+")
c = open(data_path + 'ImageSets/Main/val.txt', "w+")
d = open(data_path + 'ImageSets/Main/test.txt', "w+")

random.shuffle(all_images)

for idx, jpg_files in enumerate(all_images):
    filebase = jpg_files.rstrip(".jpg").split('/')[-1]
    # print(idx)
    if idx < train_imgs:
        a.write(str(filebase)+os.linesep)
    if idx < trainval_imgs:
        b.write(str(filebase)+os.linesep)
    if idx < val_imgs:
        c.write(str(filebase)+os.linesep)
    if idx < test_imgs:
        d.write(str(filebase)+os.linesep)
    
print('Done')
print('Moved {} files'.format(len(all_images)))