import numpy as np
import matplotlib.pyplot as plt
import cv2

img =cv2.imread("pout-dark.jpg",0)
orginal =cv2.imread("pout-dark.jpg",0)
ref_image=cv2.imread("pout-bright.jpg",0)

#print(img)


org_hist = np.zeros((256,))
org_equ_hist = np.zeros((256,))
height,width=img.shape

for i in range(width):
    for j in range(height):
        temp = orginal[j,i]
        org_hist[temp] = org_hist[temp]+1

for i in range(256):
    for j in range(i+1):
        org_equ_hist[i] += org_hist[j] * (1.0/(height*width))
    org_equ_hist[i] = round(org_equ_hist[i] * 255);

org_equ_hist=org_equ_hist.astype(np.uint8)

ref_hist = np.zeros((256,))
ref_equ_hist = np.zeros((256,))
height2,width2=ref_image.shape

for i in range(width2):
    for j in range(height2):
        temp = ref_image[j,i]
        ref_hist[temp] = ref_hist[temp]+1

for i in range(256):
    for j in range(i+1):
        ref_equ_hist[i] += ref_hist[j] * (1.0/(height2*width2))
    ref_equ_hist[i] = round(ref_equ_hist[i] * 255);

ref_equ_hist=ref_equ_hist.astype(np.uint8)




vals={}
for i in range(len(ref_equ_hist)):
    if i in vals:
        vals[i]=(vals[i]+ref_equ_hist[i])/2
    else:
        vals[i]=ref_equ_hist[i]

for i in range(width):
    for j in range(height):
        temp2 = img[j,i]
        temp3= org_equ_hist[temp2]

        for a,b in vals.items():
            if b==temp3:
                img[j,i]=a

      

final = np.concatenate((orginal, img), axis=1)
cv2.imshow('Orginal-After Histogram Matching',final)
cv2.imshow('reference',ref_image)


cv2.waitKey(0)
cv2.destroyAllWindows()