import cv2 as cv



# CONVERTING TO GREYSCALE
# img=cv.imread('imgs/two.jfif')
# cv.imshow("First",img)
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)


#bluring an image
img=cv.imread('imgs/one.jfif')
cv.imshow("First",img)
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

#edge cascade
canny=cv.Canny(blur,125,175)
cv.imshow("Canny edges",canny)


cv.waitKey(0)