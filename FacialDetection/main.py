import cv2 as cv
import copy as copy 
from ImageManager import ImageManager


image = cv.imread('human/people.jpg')
cv.imshow('Man', image)

cv.waitKey(2000)
print("DEBUG ", image[2])

imgMngr = ImageManager(image)


eyes_rect = imgMngr.findEyes()

print(f'Number of faces found = {len(eyes_rect)}')


for (x,y,w,h) in eyes_rect:
    cv.rectangle(eyes_rect, (x, y), (x + w, y + h), (0,255,0), thickness= 2)


# og = cv.resize(og, dimensions, interpolation=cv.INTER_AREA)
cv.imshow('Man', image)


cv.waitKey(0)