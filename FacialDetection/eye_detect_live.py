import cv2 as cv
import copy

from numpy import row_stack
og = cv.imread('human/white_man_side2.jpg')
cv.imshow('OG', og)
# def rotate(img, angle, rotPoint = None):
#     (height, width) = img.shape[:2]

#     if rotPoint is None:
#         rotPoint = (width//2, height//2)
    
#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimensions = (width, height)

#     return cv.warpAffine(img, rotMat, dimensions)


# og = rotate(og, 0)

gray = cv.cvtColor(og, cv.COLOR_BGR2GRAY)


haar_cascasde_eye = cv.CascadeClassifier("classifier/haarcascade_leftear.xml")

eyes_rect = haar_cascasde_eye.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=3)

print(f'Number of faces found = {len(eyes_rect)}')
eyeDetect = copy.deepcopy(og) 


for (x,y,w,h) in eyes_rect:
    cv.rectangle(eyeDetect, (x, y), (x + w, y + h), (0,255,0), thickness= 2)

width = 1470
height = (int)(eyeDetect.shape[0] * 1470/ eyeDetect.shape[1])
dimensions = (width, height)
eyeDetect = cv.resize(eyeDetect, dimensions, interpolation=cv.INTER_AREA)


cv.imshow('Detected eyes', eyeDetect)

cv.waitKey(0)