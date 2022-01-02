import cv2 as cv
img=cv.imread('imgs/1.jfif')


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("tda",gray)
cv.waitKey(0)