#image concatenator for training data images
"""
Created on Tue Nov 14 13:05:39 2023

@author: seanchang
"""
import numpy as np
from PIL import Image
import os, os.path

input_imgs = []
path = "inputs"
valid_images = [".jpg",".gif",".png",".tga", ".jpeg"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    input_imgs.append(Image.open(os.path.join(path,f)))

real_imgs = []
path = "reals"
valid_images = [".jpg",".gif",".png",".tga", ".jpeg"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    real_imgs.append(Image.open(os.path.join(path,f)))

try:
    os.mkdir("train")
except:
    print("Directory train/ already created")

counter = 0
for i, r in zip(input_imgs, real_imgs):
    stackedImg = Image.fromarray(np.concatenate((r, i), axis=1))
    stackedImg.save("train/" + str(counter) + ".jpeg", "JPEG")
    counter = counter + 1
    