
import sys
import cv2 as cv
sys.path.append('FacialDetection')
from ImageManager import ImageManager
from helperFunctions import *


image = cv.imread(r'D:\workspace\git\Python_FacialReg\FacialDetection\testingParts\testImages\people.jpg')

imgMngr = ImageManager(image)        


detector = imgMngr.haarcascade_eye

# Debug at 0 degree
angle = 0
rotatedImage = rotateCounterClockwise(image, angle)


(detected, rotatedCenter) = imgMngr.runHaarDetectionAngle(detector, angle, 1.1, 10)

for detectedArea in detected:
    (x,y) = (int(detectedArea.upperLeft.x), int(detectedArea.upperLeft.y))
    (w,h) = detectedArea.dimensions
    cv.rectangle(rotatedImage, (x, y), (x + w, y + h), (0,255,0), thickness= 2)

cv.imshow("RotatedImage w detectedArea " + str(angle), resizeToMin500(rotatedImage))

imgMngr.translateCoordinatesToOG(rotatedCenter, detected, angle)


# Debug at 90 degree
angle = 90
rotatedImage = rotateCounterClockwise(image, angle)


(detected, rotatedCenter) = imgMngr.runHaarDetectionAngle(detector, angle, 1.1, 10)

for detectedArea in detected:
    (x,y) = (int(detectedArea.upperLeft.x), int(detectedArea.upperLeft.y))
    (w,h) = detectedArea.dimensions
    cv.rectangle(rotatedImage, (x, y), (x + w, y + h), (0,255,0), thickness= 2)

cv.imshow("RotatedImage w detectedArea " + str(angle), resizeToMin500(rotatedImage))

imgMngr.translateCoordinatesToOG(rotatedCenter, detected, angle)


# Debug at 180 degree
angle = 180
rotatedImage = rotateCounterClockwise(image, angle)


(detected, rotatedCenter) = imgMngr.runHaarDetectionAngle(detector, angle, 1.1, 10)

for detectedArea in detected:
    (x,y) = (int(detectedArea.upperLeft.x), int(detectedArea.upperLeft.y))
    (w,h) = detectedArea.dimensions
    cv.rectangle(rotatedImage, (x, y), (x + w, y + h), (0,255,0), thickness= 2)


cv.imshow("RotatedImage w detectedArea " + str(angle), resizeToMin500(rotatedImage))

imgMngr.translateCoordinatesToOG(rotatedCenter, detected, angle)


# Debug at 270 degree
angle = 270
rotatedImage = rotateCounterClockwise(image, angle)


(detected, rotatedCenter) = imgMngr.runHaarDetectionAngle(detector, angle, 1.1, 10)

for detectedArea in detected:
    (x,y) = (int(detectedArea.upperLeft.x), int(detectedArea.upperLeft.y))
    (w,h) = detectedArea.dimensions
    cv.rectangle(rotatedImage, (x, y), (x + w, y + h), (0,255,0), thickness= 2)

cv.imshow("RotatedImage w detectedArea " + str(angle), resizeToMin500(rotatedImage))

imgMngr.translateCoordinatesToOG(rotatedCenter, detected, angle)
cv.waitKey(0)


        
