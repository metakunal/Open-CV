#Drawing shapes, lines and text on images  
import cv2
import numpy as np

#Creating our images, zeroes => black
img = np.zeros((512,512,3),np.uint8)
#print(img)
#colouring the images, img[:]=colour code means the whole image
#img[:]= 255,0,0
#img[200:300,200:400]=255,0,0 (This line just colours the specified area) 

#Drawing a line cv2.line(imageName, starting point, Ending Point, Colour of Line, Thickness)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
#Drawing a Rectangle, Same Convention as Line, 
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
#cv2.circle(imgName,center,radius,color,thickness)
cv2.circle(img,(400,50),30,(255,255,0),5)
#For putting text on the image
cv2.putText(img," OPENCV  ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)


cv2.imshow("Image",img)

cv2.waitKey(0)