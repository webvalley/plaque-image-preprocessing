import pandas as pd
import numpy as np
import skimage.filters as filters
from skimage.transform import rotate
from skimage.transform import resize
import matplotlib.pyplot as plt
import sklearn.preprocessing as pp
import random
import imageio
import os
'''
Random Rotation
'''
def rot(img, ang):
   #angle = random.randrange(0, 180)
   return(rotate(img, ang))
'''
Flip Horizontal
'''
def hflip(img):
    return np.fliplr(img)

'''
Flip Vertical
'''
def vflip(img):
    return np.flipud(img)
'''
Flip Diagonal
'''
def dflip(img):
    return vflip(hflip(img))
'''
Gaussian Blur
'''
def gauss(img, sig):
    return filters.gaussian(img, sigma = sig)

'''
Resize Images
'''
def rsz(img, x, y):
    return np.resize(img, (x,y,3))
'''
Crop based on ROI in CSV

def csv_crop(img, row):
    xmin = row["xmin"]
    xmax = row["xmax"]
    ymin = row["ymin"]
    ymax = row["ymax"]
    img = img[ymin:ymax, xmin:xmax]
    return (img, row["name"])
'''    
plaque_images = "./Data/Patches/Plaque/"
patch_images = "./Data/Patches/NoPlaque/"
csv_images = "./Data/CSVs/"
aug_images ="./Data/Patches/Plaque/Aug/"
folder = (os.path.join(plaque_images, file_path) for file_path in os.listdir(plaque_images))
for counter, file_path in enumerate(folder):
    if('.png' in file_path):
        img = np.array(imageio.imread(file_path))
        path = os.path.join(csv_images, (file_path.split("/")[-1][9:-4]+'.csv'))
        train = pd.read_csv(path)
        ct = 0
        for _,row in train.iterrows():    
            if(row['name'] == 'Calcific plaque'):
                classify = 'cal/'
            elif(row['name'] == 'Fibrous plaque'):
                classify = 'fibrous/'
            else:
                classify = ''
            img_name = (aug_images + classify + file_path.split("/")[-1][:-4]+"_"+row['name']+str(ct)) 
            img = rsz(img, 64,64)
            np.save(img_name+"_rsz.npy", img)
            img_rot90 = rot(img, 90)
            np.save(img_name+"_rot90.npy", img_rot90)
            img_rot270 = rot(img, 270)
            np.save(img_name+"_rot270.npy", img_rot270)
            img_hflip = hflip(img)
            ct += 1
        np.save(img_name+"_hflip.npy", img_hflip)
        img_vflip = vflip(img)
        np.save(img_name+"_vflip.npy", img_vflip)
        img_dflip = dflip(img)
        np.save(img_name+"_dflip.npy", img_dflip)
        img_gauss = gauss(img, 10)
        np.save(img_name+"_gauss.npy", img_gauss)
        
        '''
            print(file_path)
                path = os.path.join('./CSVs/',(file_path.split("/")[-1][:-4]+'.csv'))
                print(path)                
                

                train = pd.read_csv(path)
                ct = 0
                for _,row in train.iterrows():
                    print(row)
                    [img,cls] = csv_crop(img, row)
                    ct = str(ct)
                    np.save(aug_images[aug_num-1] + file_path.split("/")[-1][:-4]+"_"+cls+ct+".npy", img)
                    print(img.shape)
                    img_rot90 = rot(img, 90)
                    np.save(aug_images[aug_num-1] + file_path.split("/")[-1][:-4]+"_"+cls+ct+"_rot90.npy", img_rot90)
                    img_rot270 = rot(img, 270)
                    np.save(aug_images[aug_num-1] + file_path.split("/")[-1][:-4]+"_"+cls+ct+"_rot270.npy", img_rot270)
                    img_hflip = hflip(img)
                    np.save(aug_images[aug_num-1] + file_path.split("/")[-1][:-4]+"_"+cls+ct+"_hflip.npy", img_hflip)
                    img_vflip = vflip(img)
                    np.save(aug_images[aug_num-1] + file_path.split("/")[-1][:-4]+"_"+cls+ct+"_vflip.npy", img_vflip)
                    img_dflip = dflip(img)
                    np.save(aug_images[aug_num-1] + file_path.split("/")[-1][:-4]+"_"+cls+ct+"_dflip.npy", img_dflip)
        
        img = rsz(img, 64,64)
        np.save(img_name, img)
        img_rot90 = rot(img, 90)
        np.save(img_name, img_rot90)
        img_rot270 = rot(img, 270)
        np.save(img_name, img_rot270)
        img_hflip = hflip(img)
        np.save(img_name, img_hflip)
        img_vflip = vflip(img)
        np.save(img_name, img_vflip)
        img_dflip = dflip(img)
        np.save(img_name, img_dflip)
        img_gauss = gauss(img, 10)
        np.save(img_name, img_gauss)
        #img_gauss = gauss(img_, 20)
        #np.save(aug_images + file_path.split("/")[-1][:-4]+"_gauss20.npy", img_gauss)
	'''
