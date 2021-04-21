import numpy as np
import cv2
def bilinear_interpolate(array_in, width_in, height_in, array_out, width_out, height_out):
    for i in range(height_out):
        for j in range(width_out):
            
            x_out = j / width_out
            y_out = i / height_out


            x_in = (x_out * width_in)
            y_in = (y_out * height_in)


            x_prev = int(np.floor(x_in))
            x_next = x_prev + 1
            y_prev = int(np.floor(y_in))
            y_next = y_prev + 1

            x_prev = min(x_prev, width_in - 1)
            x_next = min(x_next, width_in - 1)
            y_prev = min(y_prev, height_in - 1)
            y_next = min(y_next, height_in - 1)
            

            dy_next = y_next - y_in;
            dy_prev = 1. - dy_next; 

            dx_next = x_next - x_in ;

            dx_prev = 1. - dx_next; 
            

            for k in range(3):    
                array_out[i][j][k] =  (array_in[y_next][x_prev][k] * dx_next* dy_prev) + (array_in[y_next][x_next][k] * dx_prev* dy_prev) +  (array_in[y_prev][x_prev][k] * dx_next *dy_next )+ (array_in[y_prev][x_next][k] * dx_prev *dy_next)

    return array_out

img =cv2.imread("lena_color.tiff")
s1 = np.zeros(shape=(int(img.shape[1]*1),int(img.shape[0]*1),3))
s2 = np.zeros(shape=(int(img.shape[1]*.5),int(img.shape[0]*.5),3))
s3 = np.zeros(shape=(int(img.shape[1]*2),int(img.shape[0]*2),3))
bilinear_interpolate(img,img.shape[1],img.shape[0], s1,img.shape[1]*1,img.shape[0]*1)
bilinear_interpolate(img,img.shape[1],img.shape[0], s2,int(img.shape[1]*.5),int(img.shape[0]*.5))
bilinear_interpolate(img,img.shape[1],img.shape[0], s3,int(img.shape[1]*2),int(img.shape[0]*2))

cv2.imshow('orginal ',img)
cv2.waitKey(0)

cv2.imwrite("scale_1.png",s1)
s1=cv2.imread("scale_1.png")
cv2.imshow('scale - 1',s1)
s1_ib = cv2.resize(img,None,fx=1,fy=1)
cv2.imshow("Inbuilt scale 1",s1_ib)
cv2.waitKey(0)

cv2.imwrite("scale_p5.png",s2)
s2=cv2.imread("scale_p5.png")
cv2.imshow('scale - 0.5',s2)
s2_ib = cv2.resize(img,None,fx=0.5,fy=0.5)
cv2.imshow("Inbuilt scale 0.5",s2_ib)
cv2.waitKey(0)

cv2.imwrite("scale_2.png",s3)
s3=cv2.imread("scale_2.png")
cv2.imshow('scale1 - 2',s3)
s3_ib = cv2.resize(img,None,fx=2,fy=2)
cv2.imshow("Inbuilt scale 2",s3_ib)
cv2.waitKey(0)


cv2.destroyAllWindows()