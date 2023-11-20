# library 
from PIL import Image 
import matplotlib.pyplot as plt 
import os
import random

rand_val=[]

def concatinate(image1,image2,loc,num):
    randy=random.randint(0, 3)
    img = Image.open(image1) 
    img1 = Image.open(image2) 
    img.size 
    img1.size 
    img_size = img.resize((256, 128)) 
    img1_size = img1.resize((256, 128)) 
    
    img2 = Image.new("RGB", (512, 256), "white") 
      
    #pasting the first image (image_name, 
    #(position)) 
    img2.paste(img_size, (0, 0)) 
      
    #pasting the second image (image_name, 
    #(position)) 
    img2.paste(img1_size, (250, 0)) 
    if randy==1:
        rand_val.append(img2)
    img2.save(loc+f"{num}.png")
    
    
#EX of Base directory Change as needed!!!!!!!!
base_dir="E:\Magic_Pen"   
    
os.makedirs(base_dir+r"\GAN\Data",exist_ok=True)
os.makedirs(base_dir+r"\GAN\Data\test",exist_ok=True)
os.makedirs(base_dir+r"\GAN\Data\train",exist_ok=True)
os.makedirs(base_dir+r"\GAN\Data\val",exist_ok=True)
  
    

test_HED=os.listdir(base_dir+r"\Vectorization\outputs\sampling\CityLine\HED\Test")
train_HED=os.listdir(base_dir+r"\Vectorization\outputs\sampling\CityLine\HED\Train")

test_vec=os.listdir(base_dir+r"\Vectorization\outputs\sampling\CityLine\Vec_Pred\Test")
train_vec=os.listdir(base_dir+r"\Vectorization\outputs\sampling\CityLine\Vec_Pred\Train")

count=0

#Save train files
for i in range(len(test_HED)):
    temp_dir=os.listdir(base_dir+f"\\Vectorization\\outputs\\sampling\CityLine\\Vec_Pred\\Test\\{i}")
    for j in range(len(temp_dir)):
        concatinate(base_dir+f"\\Vectorization\\outputs\\sampling\CityLine\\Vec_Pred\\Test\\{test_vec[i]}\\{temp_dir[j]}", base_dir+"\\Vectorization\\outputs\\sampling\\CityLine\\HED\\Test\\"+test_HED[i], base_dir+"\\GAN\\Data\\test\\",count)
        count+=1
        

#Save Test Files
count=0
for i in range(len(train_HED)):
    temp_dir=os.listdir(base_dir+f"\\Vectorization\\outputs\\sampling\CityLine\\Vec_Pred\\Train\\{train_vec[i]}")
    for j in range(len(temp_dir)):
        concatinate(base_dir+f"\\Vectorization\\outputs\\sampling\CityLine\\Vec_Pred\\Train\\{train_vec[i]}\\{temp_dir[j]}", base_dir+"\\Vectorization\\outputs\\sampling\\CityLine\\HED\\Train\\"+train_HED[i], base_dir+"\\GAN\\Data\\train\\",count)
        count+=1

for i in range(len(rand_val)):
    rand_val[i].save(base_dir+"\\GAN\\Data\\val\\"+f"{i}.png")
    

