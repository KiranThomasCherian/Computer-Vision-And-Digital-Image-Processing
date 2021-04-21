import numpy as np
import matplotlib.pyplot as plt
import cv2

img =cv2.imread("pout-dark.jpg",0)
orginal=cv2.imread("pout-dark.jpg",0)



org_hist = np.zeros((256,))
norm_hist = np.zeros((256,))
height,width=img.shape

for i in range(width):
    for j in range(height):
        temp = img[j,i]
        org_hist[temp] = org_hist[temp]+1



for i in range(256):
    for j in range(i+1):
        norm_hist[i] += org_hist[j] * (1.0/(height*width))
    norm_hist[i] = round(norm_hist[i] * 255);

norm_hist=norm_hist.astype(np.uint8)



for i in range(width):
    for j in range(height):
        temp2 = img[j,i]
        img[j,i]= norm_hist[temp2]

final = np.concatenate((orginal, img), axis=1)
cv2.imshow('Orginal-After Equalization',final)

plt.hist(orginal.ravel(), bins=256,)
plt.title("HISTOGRAMS")
plt.hist(img.ravel(),bins=256,)
plt.show()
cv2.waitKey(0) 

cv2.destroyAllWindows()