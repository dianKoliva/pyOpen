import cv2 as cv
import numpy as np


blank=np.zeros((400,400),dtype='uint8')
rec=cv.rectangle(blank.copy)

cv.waitKey(0)