import cv2
import numpy as np

img = cv2.imread("Photos/puppy.jpg")
print(img.shape) #To know the size of our image

#Resizing Function
imgResize = cv2.resize(img,(1000,500))
print(imgResize.shape)

#For cropping the image, the image is basically a matrix or array, so can crop that using matrix only
#img[46:119,352:495] => means width cropped from 46 to 119 and height from 352 to 495
imgCropped = img[46:119,352:495]
print(imgCropped.shape)

# cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)