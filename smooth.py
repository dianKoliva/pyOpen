import cv2 as cv 

img =cv.imread('imgs/large.jfif')

avrg=cv.blur(img,(5,5))
cv.imshow("avg",avrg)

cv.waitKey(0)