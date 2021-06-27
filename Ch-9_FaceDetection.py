import cv2

#Importing Face Cascade Provided by open-CV to detect faces
faceCascade= cv2.CascadeClassifier("Photos/haarcascade_frontalface_default.xml")
img = cv2.imread('Photos/lena.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

#Drawing bounding box around the faces we have detected
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow("Result", img)
cv2.waitKey(0)