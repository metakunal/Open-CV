import cv2
print("Package Imported")

#For reading images function used-imread (Function Parameter is Path)
#Here we have created a variable img to store our image.
img = cv2.imread("Photos/puppy.jpg") 


#For displaying image- function used - imshow("Window Name",image)
cv2.imshow("Output",img)

#The image appears and dissapears immediately, so we need to add a waiting time.(0-infinite, everyhting else is in millisecond)
#Remember the camel-casing of waitkey(X) and waitKey(✔) 
cv2.waitKey(0)