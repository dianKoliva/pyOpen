import cv2 as cv 

img =cv.imread('imgs/two.jfif')
# cv.imshow("Image",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#bgr to hsv 
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hv",hsv)

cv.waitKey(0)