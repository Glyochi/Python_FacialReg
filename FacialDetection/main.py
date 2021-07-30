
import cv2 as cv
import copy as copy 
import sys
sys.path.append('FacialDetection')
from helperFunctions import *
from ImageManager import ImageManager


image = cv.imread('human\people2.jpg')
image2 = cv.imread('human\people2.jpg')
# image = resizeMinTo(image,800)
# print("DEBUG ", image[2])

imgMngr = ImageManager(image)


# eyes_rect = imgMngr.findPairsOfEyes(1.1, 10)

# print(f'Number of eyes found = {len(eyes_rect)}')

# for pair in eyes_rect:
#     pair[0].draw(image, (0,255,0), thickness= 2)
#     pair[1].draw(image, (0,255,0), thickness= 2)

# faces_rect = imgMngr.findFacesUsingPairOfEyes(eyes_rect, 1.1, 10)
faces_rect = imgMngr.findFaces(1.1, 10)

for face in faces_rect:
    face.draw(image, (0,0,255), thickness= 2)

image2Gray = cv.cvtColor(image2, cv.COLOR_BGR2GRAY)
faces_rect_default = imgMngr.haarcascade_face.detectMultiScale(image2Gray, 1.1, 10)

for (x,y,w,h) in faces_rect_default:
    cv.rectangle(image2, (x,y), (x + w, y + h), (0,255,0), 2)

# og = cv.resize(og, dimensions, interpolation=cv.INTER_AREA)
cv.imshow('My method', image)
cv.imshow('Default method', image2)


cv.waitKey(0)