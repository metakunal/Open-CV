import cv2
import numpy as np

img = cv2.imread("Photos/puppy.jpg")
#kernel is to be used in Dilation and Eroded function
#np.ones= The matrix will contain all ones.(5,5) is the size of the matrix. np.unit8 => Unsigned Integer of 8-bit (8bit => Values ranging from 0 to 255)
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Gray Image
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) #to Blur the Image
imgCanny = cv2.Canny(img,150,200) #For Edge Detection
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1) #make the image thicker for better edge detection, iteration=> thickness
imgEroded = cv2.erode(imgDialation,kernel,iterations=1) #opposite of Dialation, makes the image thinner

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)