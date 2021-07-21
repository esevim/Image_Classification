#Randomly pick and copy 20 images per each class.

import os
import shutil
import random

root = 'C:/Erdem PC External/GBC/13-DL-2/Project/Data'
os.makedirs(f'{root}/training/training200')

root_path200 = f'{root}/training/training200'
folders = ['n0', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9']
for folder in folders:
    os.mkdir(os.path.join(root_path200,folder))


    
for i in range(10):
    src = f'{root}/training/training/n' + str(i)
    src_files = random.sample(os.listdir(src), 20)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        shutil.copy(full_file_name, f'{root}/training/training200/n' + str(i))