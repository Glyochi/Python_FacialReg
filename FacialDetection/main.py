
import cv2 as cv
import copy as copy 
import sys
sys.path.append('FacialDetection')
from helperFunctions import *
from ImageManager import ImageManager


image = cv.imread('human\people.jpg')
cv.imshow('Man', image)
# image = resizeMinTo(image,800)
# print("DEBUG ", image[2])

imgMngr = ImageManager(image)


eyes_rect = imgMngr.findPairsOfEyes(1.1, 10)

print(f'Number of eyes found = {len(eyes_rect)}')

for pair in eyes_rect:
    print("-----------------------------------")
    print(pair[0])
    print(pair[1])
    print(pair[2])
    pair[0].draw(image, (0,255,0), thickness= 2)
    pair[1].draw(image, (0,255,0), thickness= 2)


# og = cv.resize(og, dimensions, interpolation=cv.INTER_AREA)
cv.imshow('Man', image)


cv.waitKey(0)