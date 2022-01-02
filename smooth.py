import cv2 as cv 

img =cv.imread('imgs/large.jfif')

# averaging
avrg=cv.blur(img,(5,5))
# cv.imshow("avg",avrg)

#gausian blur
gauss=cv.GaussianBlur(img,(5,5),0)
# cv.imshow("avg",gauss)


# median blur
med=cv.medianBlur(img,3)
cv.imshow("avg",med)
cv.waitKey(0)