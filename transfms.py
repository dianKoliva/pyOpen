import cv2 as cv
import numpy as np
img=cv.imread('imgs/one.jfif')
# cv.imshow("First",img)

cv.waitKey(0)

def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# -x--left
# -y --upshift
# x shift to right 
# y  shift down 
# translating
translated =translate(img,-200,-200)
# cv.imshow("trans",translated)

# rotation
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)

    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,45)
# cv.imshow('rotated',rotated)

# resize image
resized =cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)

cv.waitKey(0)