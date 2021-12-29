import cv2 as cv 
import numpy as np

# create blank image
blank=np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Blank',blank)

# paint the color
# blank[200:300,300:400]=0,255,0
# cv.imshow('Green',blank)

# # draw rectangle
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,250,0),thickness=-1)
# cv.imshow('Rect',blank)

#draw a circle
cv.circle(blank,(250,250),40,(0,0,250),thickness=3)
cv.show('Circl',blank)

cv.waitKey(0)