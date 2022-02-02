
# > Computer Vision And Digital Image Processing Course Works and Projects

------------------------------------------------------------------------------------

# Computer Vision
Computer Vision course works

------------------------------------------------------------------------------------

## Assignment 1:

Q1: Take an image.
a. Convert that into gray scale and that gray scale into binary using builtin functions and display all three in single window.
b. Find the minimum and maximum 
    i.  in the color image (for green, red and blue channel) 
    ii. in the gray scale image
    iii. in the binary image

Q2: Write the python program which takes two polynomial as input and output the product of those two polynomials using convolution in spatial domain
(in O(n^2))

## Assignment 2:

1. a. Take an image of the wall of your house and apply a sobel filter and count the number of edge pixels in the edge map
b. Do the same operation for the image of a tree ( capture your own image of the tree ) and report your observation on the two images

2. Each of the images considered in the first problem apply Gaussian filters of size 7*7, 9*9 and 11*11. Repeat the problem 1 and report your observation

## Assignment 3:

Capture Image of chess board(in Black & white) . The captured imageneeds to be converted to gray scale and then to black and white. Write a python script to find all the corner points in the binary chess board image, anddisplay integer coordinates at each corner, superimposing the coordinates with the binary image.
(0,0) needs to be displayed at topmost and left most corner, and (8,8) is to be displayed at the lastcorner

## Assignment 4:

Design and implement the scheme to find the disparity map from the stereo images. Consider the given images for the test case. You are allowed to use inbuilt functions. 

## Assignment 5:

Camera calibration using builtin function. 
Hint:Chessboard can be used for imaging  purpose

## Assignment 6:

Implement the watershed algorithm in openCV

## Assignment 7:

Problem Description:

All the images attached along with this show cells identifiable by their well-stained nuclei. The nuclei are stained either blue or brown.
The diagnosis report is defined as follows:  
percentage positivity =  percentage of Total nuclei that are brown in color / Total nuclei in the picture (blue & brown inclusive)
Write a program to find the percentage of positivity in the image given below and classify into grade the level of cancer, using the thresholding scheme followed in the convention method, which is detailed below.

Currently, we see the image in the microscope, count and calculate the %, manually. This is not reproducible always and is subjective. Idea is to make it objective. 
The gold standard is to take prints and manually count on the images and many studies show that this is objective. To save on paper and time, we want the software to do the job. Brown nuclei indicate that they express the immune marker called Ki67 and the higher the percentage positivity, the more aggressive it is considered to be. In many cases, a cut-off is used to grade cancer. For example <15% is considered low grade and >15% as high grade. Treatment and follow-up actions differ in these 2 situations. Hence, the real problem is with borderline percentages (between 20 & 30% on manual counts). We expect the software to give more accurate and reproducible results.
Here the software must do 2 things
1) Identify percentage positivity (similar to that described above)
2) Classify the intensity of staining as low and high grade.


## Assignment 8:

Face recognition using SIFT features and the demo should be shown on students' faces.


------------------------------------------------------------------------------------

# Digital-Image-Processing
Digital Image Processing course works

------------------------------------------------------------------------------------

## Assignment 1:

3. Take a Lena image and convert it into grayscale. Add three different types of noises(salt and pepper, additive Gaussian noise, speckle), each noise in the sets of 5,10,15,20,25,30. Take average for each set and display the average images. Report the observation made.

4. Download Lena image and scale it by factors of 1,2,0.5 using bilinear interpolation and display the scaled images. Also, display the output of built-in functions for doing scaling by factors of 0.5,2. Compare the results.

5. Download the leaning tower of PISA image and find the angle of inclination using appropriate rotations with bilinear interpolation.

6. Do histogram equalization on pout-dark and display the same

7. Do histogram matching(specification) on the pout-dark image, keeping pout-bright as a reference image

------------------------------------------------------------------------------------

## Assignment 2:

1. Download Lena color image convert it to grayscale image and add salt and  pepper noise with noise quantity 0.1,0.2 upto 1 and generate 10 noisy images.

>a. Do average filtering ( by correlating with average filter ) of varying sizes for each image. Filter size can be 3*3, 5*5, 7*7. (In 3*3 filter all the values are 1/9, in 5*5 filter all the values are 1/25 and in 7*7 filter all the values are 1/49)

>b. Similarly, repeat the question 1.a by replacing the average filter by median filter.


2.Correlation

>a. Consider the image the attached named as hdraw.png and crop each of the characters from the image and consider that as the sub-image. Find the location of the sub-image in the original by using correlation.

>b. Download Lena color image convert it to grayscale image and crop the left eye of Lena as sub-image and do the cross-correlation ( Normalized correlation) to find the location of the left eye in the original image.

3. Write a function to implement FFT for 1D signal.

4. Implement DFT function for an image using the FFT for 1D signal using question 3.

5. Consider the images of lena and dog images attached. Find phase and magnitude of the dog and lena images using DFT function implemented in question 4.

6. Swap phase of the dog image and magnitude of the lena image and display the output.

7. Swap phase of the lena image and magnitude of the dog image ad display the output


------------------------------------------------------------------------------------


# Project - OCR Web Application Using Flask and Tesseract

>A web application that lets you extract text from an input image. 
>The image is extracted using the tesseract optical character recognition engine. 
>We also provide the results after noise removal using median blur, and after morphological operations like erosion followed by dilation, and the user can copy the best option.

Project Files:https://github.com/fathimanourin/OCR-webapp

# Project - Panorama Stitching

>A flask web application to create a panorama image from user inputs,using SIFT to detect keypoints , and homography matrix to apply the transformation

Project Files:https://github.com/sherinkk/Panorama_Stitching
