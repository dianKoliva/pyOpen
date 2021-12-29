import cv2 as cv

# resclaling images
# img=cv.imread('imgs/one.jfif')
# cv.imshow("First",img)

def rescaleFrame(frame,scale=0.1):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)



def changeRes(width,height):
    #works for live video only
    capture.set(3,width)
    capture.set(4,height)




capture=cv.VideoCapture('vids/one.mp4')
while True:
    isTrue, frame=capture.read()
    
    frame_resized=rescaleFrame(frame)

    cv.imshow('Video',frame)
    cv.imshow('Risized vid',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
