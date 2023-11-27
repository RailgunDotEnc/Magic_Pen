# library 
from PIL import Image 
import matplotlib.pyplot as plt 
import os
import random

rand_val=[]

def concatinate(image1,image2,loc,num):
    randy=random.randint(0, 3)
    img = Image.open(image2) 
    img1 = Image.open(image1) 
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
    
    
base_dir="E:\Magic_Pen"   
    
os.makedirs(base_dir+r"\GAN\Data_Pred",exist_ok=True)
os.makedirs(base_dir+r"\GAN\Data_Pred\test",exist_ok=True)
os.makedirs(base_dir+r"\GAN\Data_Pred\train",exist_ok=True)
os.makedirs(base_dir+r"\GAN\Data_Pred\val",exist_ok=True)
  
    


test_vec=os.listdir(base_dir+r"\Vectorization\outputs\sampling\CityLine\Vec_Pred\Test")
train_vec=os.listdir(base_dir+r"\Vectorization\outputs\sampling\CityLine\Vec_Pred\Train")

count=0
for i in range(len(test_vec)):
    temp_dir=os.listdir(base_dir+f"\\Vectorization\\outputs\\sampling\CityLine\\Vec_Pred\\Test\\{test_vec[i]}")
    for j in range(len(temp_dir)-1):
        concatinate(base_dir+f"\\Vectorization\\outputs\\sampling\CityLine\\Vec_Pred\\Test\\{test_vec[i]}\\{temp_dir[j]}", base_dir+f"\\Vectorization\\outputs\\sampling\CityLine\\Vec_Pred\\Test\\{test_vec[i]}\\{temp_dir[j+1]}", base_dir+"\\GAN\\Data_Pred\\test\\",count)
        print(temp_dir[j],temp_dir[j+1],count)
        count+=1
count=0    
print()
for i in range(len(train_vec)):
    temp_dir=os.listdir(base_dir+f"\\Vectorization\\outputs\\sampling\CityLine\\Vec_Pred\\train\\{train_vec[i]}")
    for j in range(len(temp_dir)-1):
        concatinate(base_dir+f"\\Vectorization\\outputs\\sampling\CityLine\\Vec_Pred\\Train\\{train_vec[i]}\\{temp_dir[j]}", base_dir+f"\\Vectorization\\outputs\\sampling\CityLine\\Vec_Pred\\Train\\{train_vec[i]}\\{temp_dir[j+1]}", base_dir+"\\GAN\\Data_Pred\\train\\",count)
        print(temp_dir[j],temp_dir[j+1],count)
        count+=1
        
for i in range(len(rand_val)):
    rand_val[i].save(base_dir+"\\GAN\\Data_Pred\\val\\"+f"{i}.png")
    

