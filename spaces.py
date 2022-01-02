import cv2 as cv 

img =cv.imread('imgs/one.jfif')
cv.imshow("Image",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

cv.waitKey(0)