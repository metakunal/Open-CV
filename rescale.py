import cv2 as cv;

img = cv.imread('Photos/puppy.jpg')
cv.imshow('Puppy',img)

def rescaleFrame(frame, scale = 0.75) :
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#waitKey is a keyboard binding funcion, wait for infinite amount of time for a key to be pressed
cv.waitKey(0)