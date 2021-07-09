import cv2 as cv
import copy as copy 
og = cv.imread('human/Man_side.jpg')


gray = cv.cvtColor(og, cv.COLOR_BGR2GRAY)


haar_cascasde_face = cv.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")

faces_rect = haar_cascasde_face.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')
faceDetect = copy.deepcopy(og) 


for (x,y,w,h) in faces_rect:
    cv.rectangle(faceDetect, (x, y), (x + w, y + h), (0,255,0), thickness= 2)

width = 1470
height = (int)(faceDetect.shape[0] * 1470/ faceDetect.shape[1])
dimensions = (width, height)
faceDetect = cv.resize(faceDetect, dimensions, interpolation=cv.INTER_AREA)


# og = cv.resize(og, dimensions, interpolation=cv.INTER_AREA)
cv.imshow('Man', og)

cv.imshow('Detected face', faceDetect)

cv.waitKey(0)