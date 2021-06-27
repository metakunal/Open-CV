#pylint:disable=no-member

import cv2 as cv
import numpy as np

img = cv.imread('Photos/puppy.jpg')
cv.imshow('Puppy', img)

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

cv.waitKey(0)