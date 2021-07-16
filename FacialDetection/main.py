import cv2 as cv
import copy as copy 
from ImageManager import ImageManager


image = cv.imread('human\people.jpg')
cv.imshow('Man', image)

print("DEBUG ", image[2])

imgMngr = ImageManager(image)


eyes_rect = imgMngr.findEyes()

print(f'Number of faces found = {len(eyes_rect)}')


for detectedArea in eyes_rect:
    print(f'Debug upperLeft', detectedArea.upperLeft.x, " and ", detectedArea.upperLeft.y)
    print(f'Debug dimension', detectedArea.dimensions[0], " and ", detectedArea.dimensions[1])
    (x,y) = (int(detectedArea.upperLeft.x), int(detectedArea.upperLeft.y))
    (w,h) = detectedArea.dimensions
    cv.rectangle(image, (x, y), (x + w, y + h), (0,255,0), thickness= 2)


# og = cv.resize(og, dimensions, interpolation=cv.INTER_AREA)
cv.imshow('Man', image)


cv.waitKey(0)