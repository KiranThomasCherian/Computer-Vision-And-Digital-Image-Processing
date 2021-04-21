import cv2
import numpy as np
from skimage.util import random_noise
from random import seed
from random import random

img = cv2.imread("lena_color.tiff")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


gauss = []
sp = []
speckle = []


for j in range(1,7):
    
    temp_gauss = 0
    temp_sp = 0
    temp_speckle = 0

    for i in range(5*j):
        
        gauss_img = random_noise(img,mode='gaussian',mean=random(),var= random())
        sp_img = random_noise(img,mode='s&p',amount = random())
        speckle_img = random_noise(img,mode='speckle',mean=0,var=random())
        
        temp_gauss += gauss_img
        temp_sp += sp_img
        temp_speckle += speckle_img
         
    gauss.append(temp_gauss/(5*j))
    sp.append(temp_sp/(5*j))
    speckle.append(temp_speckle/(5*j))

    
final_gauss = np.concatenate((gauss[0],gauss[1],gauss[2]), axis=1)
final_gauss2 = np.concatenate((gauss[3],gauss[4],gauss[5],), axis=1)
cv2.imshow('Lena_Gaussian  5 , 10, 15 ',final_gauss)
cv2.imshow('Lena_Gaussian 20, 25, 30  ',final_gauss2)


final_sp = np.concatenate((sp[0],sp[1],sp[2]), axis=1)
final_sp2 = np.concatenate((sp[3],sp[4],sp[5],), axis=1)
cv2.imshow('Lena_sp  5, 10, 15  ',final_sp)
cv2.imshow('Lena_sp 20, 25, 30  ',final_sp2)


final_speckle = np.concatenate((speckle[0],speckle[1],speckle[2]), axis=1)
final_speckle2 = np.concatenate((speckle[3],speckle[4],speckle[5],), axis=1)
cv2.imshow('Lena_Speckle 5, 10, 15 ',final_speckle)
cv2.imshow('Lena_Speckle 20, 25, 30  ',final_speckle2)

cv2.waitKey(0) 
cv2.destroyAllWindows()