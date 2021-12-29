import cv2 as cv
import numpy as np
img=cv.imread('imgs/two.jfif')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# cv.imshow("cont",gray)


canny=cv.Canny(img,125,175)
cv.imshow('canny',canny)

conts,hics=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

cv.waitKey(0)