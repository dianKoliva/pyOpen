import cv2 as cv

img=cv.imread('imgs/two.jfif')
cv.imshow("First",img)

# CONVERTING TO GREYSCALE

gray=cv.cvtColor(img,cv.COLOR_BG2GRAY)
cv.imshow('Gray',gray)

cv.waitKey(0)