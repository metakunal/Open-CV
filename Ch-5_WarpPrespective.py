import cv2
import numpy as np

img = cv2.imread("Photos/cards.jpg")

width,height = 250,350
#The four corner points of the card, stored in the form of a float array
#If you want to get these values open Paint in windows, move cursor to get the values
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
#Defining out points as the origin and other coordinates
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
#The transformation MAtrix
matrix = cv2.getPerspectiveTransform(pts1,pts2)
#Using the Warp Perspective
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)