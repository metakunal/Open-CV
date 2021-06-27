import cv2

#Function to capture videos, with provide aruments as 0,1 or 2 if you want images from the webcam.
#Most probably webcam as 0, but you can use 1 or 2 if you have multiple cameras connected to your computer.
#Or you can pass the path of video as argument.
capture = cv2.VideoCapture('Videos/Dog.mp4')

#Videos are actually read by using while loops frame by frame.
while True:
    isTrue, frame = capture.read() #Read frame if detected
    cv2.imshow('Video',frame) #We can actually display aframe
        #frame is another variable we can name it anything

    #To stop the video from playing indefinetly, we have to press the key d.
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

#Not really necessary lines
capture.release()
cv2.destroyAllWindows()
