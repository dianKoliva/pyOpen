import cv2 as cv
img=cv.imread('imgs/g.jpg')


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)


haar_casc=cv.CascadeClassifier("haar_face.xml")
faces=haar_casc.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
print(f'number of faces found ={len(faces)}')
for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow("Detected faces",img)

cv.waitKey(0)