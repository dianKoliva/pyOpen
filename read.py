import cv2 as cv

# reading images
# img=cv.imread('imgs/one.jfif')
# cv.imshow("First",img)



# reading videos 

capture=cv.VideoCapture('vids/one.mp4')
while True:
    isTrue, frame=capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)
