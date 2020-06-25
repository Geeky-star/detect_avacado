import cv2

face_cascade = cv2.CascadeClassifier('haar_cascades_avacado.xml')
img = cv2.imread('download.jpg')
img = cv2.resize(img, (100,100))
faces = face_cascade.detectMultiScale(img,1.1,4)
for(x,y,w,h) in faces:
      cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
    
cv2.imshow('img',img)
cv2.waitKey()