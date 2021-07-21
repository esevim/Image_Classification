from keras.preprocessing.image import array_to_img, img_to_array, load_img
from keras.preprocessing.image import ImageDataGenerator
import os
import random

root = 'C:/Erdem PC External/GBC/13-DL-2/Project/Data/'

os.makedirs(f'{root}training/training2000')   

from distutils.dir_util import copy_tree
fromDirectory = f"{root}training/training"
toDirectory = f"{root}training/training2000"
copy_tree(fromDirectory, toDirectory)

datagen = ImageDataGenerator(
        rotation_range=60,
        width_shift_range=0.2,
        height_shift_range=0.2,
        zoom_range=0.3,
        horizontal_flip=True,
        vertical_flip = True,
        fill_mode='nearest')

for i in range(10):
    src = f'{root}training/training2000/n' + str(i)
    for each in os.listdir(src):
        imglink = each
        imglinkfull = src + '/' + imglink
        augimg = load_img(imglinkfull)
        x = img_to_array(augimg)  
        x = x.reshape((1,) + x.shape)
    
        j = 0
        for batch in datagen.flow(x, batch_size=1,
                          save_to_dir=f'{root}training/training2000/n' + str(i), 
                          save_prefix='img', 
                          save_format='jpeg'):
            j += 1
            if j >= 1:
                break  # break the loop, otherwise it will never 