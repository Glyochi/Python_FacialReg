
import sys
import cv2 as cv
sys.path.append('FacialDetection')
from ImageManager import ImageManager
from helperFunctions import *


image = cv.imread(r'D:\workspace\git\Python_FacialReg\FacialDetection\testingParts\testImages\people.jpg')

imgMngr = ImageManager(image)        

detector = imgMngr.haarcascade_eye

# constant parameter for testing
scaleFactor = 1.1
minNeighbors = 10



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Test 0, 90, 180, 270 returned detectedAreas # Test 0, 90, 180, 270 returned detectedAreas # Test 0, 90, 180, 270 returned detectedAreas # Test 0, 90, 180, 270 returned detectedAreas #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Debug at 0 degree
angle = 0
rotatedImage = rotateCounterClockwise(image, angle)


(detected0, rotatedCenter0) = imgMngr.HELPER_runHaarDetectionCounterClockwiseAngle(detector, angle, scaleFactor, minNeighbors)

for detectedArea in detected0:
    detectedArea.draw(rotatedImage, (0,255,0), thickness= 2)

cv.imshow("RotatedImage w detectedArea " + str(angle), resizeMinTo500(rotatedImage))



# Debug at 90 degree
angle = 90
rotatedImage = rotateCounterClockwise(image, angle)


(detected90, rotatedCenter90) = imgMngr.HELPER_runHaarDetectionCounterClockwiseAngle(detector, angle, scaleFactor, minNeighbors)

for detectedArea in detected90:
    detectedArea.draw(rotatedImage, (255,0,0), thickness= 2)

cv.imshow("RotatedImage w detectedArea " + str(angle), resizeMinTo500(rotatedImage))



# Debug at 180 degree
angle = 180
rotatedImage = rotateCounterClockwise(image, angle)


(detected180, rotatedCenter180) = imgMngr.HELPER_runHaarDetectionCounterClockwiseAngle(detector, angle, scaleFactor, minNeighbors)

for detectedArea in detected180:
    detectedArea.draw(rotatedImage, (0,0,255), thickness= 2)


cv.imshow("RotatedImage w detectedArea " + str(angle), resizeMinTo500(rotatedImage))



# Debug at 270 degree
angle = 270
rotatedImage = rotateCounterClockwise(image, angle)


(detected270, rotatedCenter270) = imgMngr.HELPER_runHaarDetectionCounterClockwiseAngle(detector, angle, scaleFactor, minNeighbors)

for detectedArea in detected270:
    detectedArea.draw(rotatedImage, (255,255,0), thickness= 2)

cv.imshow("RotatedImage w detectedArea " + str(angle), resizeMinTo500(rotatedImage))




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Test translatedArea in 0, 90, 180, 270 degree rotated images translation to coordinates in original image # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
This part is for testing the location of detectedAreas after each function call
"""

rotatedImage = rotateCounterClockwise(image, 0)


# for detectedArea in detected0:
#     detectedArea.draw(rotatedImage, (0,255,0), thickness= 2)
#     cv.putText(rotatedImage,'0', (int(detectedArea.center.x - 5), int(detectedArea.center.y - 5)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), thickness = 2)
# for detectedArea in detected90:
#     detectedArea.draw(rotatedImage, (255,0,0), thickness= 2)
#     cv.putText(rotatedImage,'90 V', (int(detectedArea.center.x - 5), int(detectedArea.center.y - 5)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), thickness = 2)
# for detectedArea in detected180:
#     detectedArea.draw(rotatedImage, (0,0,255), thickness= 2)
#     cv.putText(rotatedImage,'180', (int(detectedArea.center.x - 5), int(detectedArea.center.y - 5)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), thickness = 2)
# for detectedArea in detected270:
#     detectedArea.draw(rotatedImage, (255,255,0), thickness= 2)
#     cv.putText(rotatedImage,'270 V', (int(detectedArea.center.x - 5), int(detectedArea.center.y - 5)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,0), thickness = 2)


# rotatedImage = cv.circle(rotatedImage, (600, 400), 0, (255, 255, 255), 12)
# cv.putText(rotatedImage,'newCenter', (600 - 8, 400 - 16), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,0), thickness = 2)

# rotatedImage = cv.circle(rotatedImage, (400, 600), 0, (255, 255, 255), 12)
# cv.putText(rotatedImage,'rotatedCenter', (400 - 8, 600 - 16), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,0), thickness = 2)

# detectedArea = detected270[0]
# detectedArea.draw(rotatedImage, (255,255,0), thickness= 2)
# cv.putText(rotatedImage,'270 V', (int(detectedArea.center.x - 5), int(detectedArea.center.y - 5)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,0), thickness = 2)

imgMngr.HELPER_rotateDetectedAreaClockwise(detected0, rotatedCenter0, 0)
imgMngr.HELPER_rotateDetectedAreaClockwise(detected90, rotatedCenter90, 90)
imgMngr.HELPER_rotateDetectedAreaClockwise(detected180, rotatedCenter180, 180)
imgMngr.HELPER_rotateDetectedAreaClockwise(detected270, rotatedCenter270, 270)



# for detectedArea in detected0:
#     detectedArea.draw(rotatedImage, (0,255,0), thickness= 2)
#     cv.putText(rotatedImage,'0', (int(detectedArea.center.x - 5), int(detectedArea.center.y - 5)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), thickness = 2)
# for detectedArea in detected90:
#     detectedArea.draw(rotatedImage, (255,0,0), thickness= 2)
#     cv.putText(rotatedImage,'90 R', (int(detectedArea.center.x - 5), int(detectedArea.center.y - 5)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), thickness = 2)
# for detectedArea in detected180:
#     detectedArea.draw(rotatedImage, (0,0,255), thickness= 2)
# #     cv.putText(rotatedImage,'180', (int(detectedArea.center.x - 5), int(detectedArea.center.y - 5)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), thickness = 2)
# for detectedArea in detected270:
#     detectedArea.draw(rotatedImage, (255,255,0), thickness= 2)
#     cv.putText(rotatedImage,'270 R', (int(detectedArea.center.x - 5), int(detectedArea.center.y - 5)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,0), thickness = 2)
    

# detectedArea = detected270[0]
# detectedArea.draw(rotatedImage, (255,255,0), thickness= 2)
# cv.putText(rotatedImage,'270 R', (int(detectedArea.center.x - 5), int(detectedArea.center.y - 5)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,0), thickness = 2)

imgMngr.HELPER_projectDetectedArea(detected0, rotatedCenter0)
imgMngr.HELPER_projectDetectedArea(detected90, rotatedCenter90)
imgMngr.HELPER_projectDetectedArea(detected180, rotatedCenter180)
imgMngr.HELPER_projectDetectedArea(detected270, rotatedCenter270)




# for detectedArea in detected0:
#     detectedArea.draw(rotatedImage, (0,255,0), thickness= 2)
#     cv.putText(rotatedImage,'0', (int(detectedArea.center.x - 5), int(detectedArea.center.y - 5)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), thickness = 2)
# for detectedArea in detected90:
#     detectedArea.draw(rotatedImage, (255,0,0), thickness= 2)
#     cv.putText(rotatedImage,'90 F', (int(detectedArea.center.x - 5), int(detectedArea.center.y - 5)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), thickness = 2)
# for detectedArea in detected180:
#     detectedArea.draw(rotatedImage, (0,0,255), thickness= 2)
#     cv.putText(rotatedImage,'180', (int(detectedArea.center.x - 5), int(detectedArea.center.y - 5)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), thickness = 2)
# for detectedArea in detected270:
#     detectedArea.draw(rotatedImage, (255,255,0), thickness= 2)
#     cv.putText(rotatedImage,'270 F', (int(detectedArea.center.x - 5), int(detectedArea.center.y - 5)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,0), thickness = 2)

# detectedArea = detected270[0]
# detectedArea.draw(rotatedImage, (255,255,0), thickness= 2)
# cv.putText(rotatedImage,'270 F', (int(detectedArea.center.x - 5), int(detectedArea.center.y - 5)), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,0), thickness = 2)




# Draw pre-merging

for detectedArea in detected0:
    detectedArea.draw(rotatedImage, (0,255,0), thickness= 2)
for detectedArea in detected90:
    detectedArea.draw(rotatedImage, (255,0,0), thickness= 2)
for detectedArea in detected180:
    detectedArea.draw(rotatedImage, (0,0,255), thickness= 2)
for detectedArea in detected270:
    detectedArea.draw(rotatedImage, (255,255,0), thickness= 2)

cv.imshow("All detected Eyes separated", resizeMinTo500(rotatedImage))



# Merge the overlapping detectedAreas

rotatedImage = rotateCounterClockwise(image, 0)
detectedEyes = (detected0, detected90, detected180, detected270)
detectedEyes = imgMngr.HELPER_mergeDetectedObjs(detectedEyes)

for detectedEye in detectedEyes:
    detectedEye.draw(rotatedImage, (255, 255, 255), 2)
cv.imshow("Merged detected Eyes", resizeMinTo500(rotatedImage))



# Find the faces using detectedEyes

rotatedImage = rotateCounterClockwise(image, 0)
detectedEyes = imgMngr.findPairsOfEyes(1.1, 10)



DebugFaces = imgMngr.DEBUGfindFacesUsingPairOfEyes(detectedEyes, 1.1, 10)

for i in range(len(DebugFaces)):
    (face, rotatedFaceOrigin, croppedCenter, rotatedImageCenter, relativeAngle, originalImageCenter)  = DebugFaces[i]
    face.draw(rotatedImage, (255, 0, 0), 2)
    cv.putText(rotatedImage, str(i), face.upperLeft.exportCoordinates(), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

cv.imshow("Raw faces' coordinates", resizeMinTo500(rotatedImage))


# First projection

rotatedImage = rotateCounterClockwise(image, 0)

for i in range(len(DebugFaces)):
    (face, rotatedFaceOrigin, croppedCenter, rotatedImageCenter, relativeAngle, originalImageCenter)  = DebugFaces[i]
    face.projectArea(croppedCenter, rotatedFaceOrigin)
    face.draw(rotatedImage, (0, 255, 0), 2)
    cv.putText(rotatedImage, str(i), face.upperLeft.exportCoordinates(), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv.imshow("After first projection", resizeMinTo500(rotatedImage))

# First projection and rotate

rotatedImage = rotateCounterClockwise(image, 0)

for i in range(len(DebugFaces)):
    (face, rotatedFaceOrigin, croppedCenter, rotatedImageCenter, relativeAngle, originalImageCenter)  = DebugFaces[i]
    face.rotateAreaCounterClockwise(rotatedImageCenter, relativeAngle)
    face.draw(rotatedImage, (0, 0, 255), 2)
    cv.putText(rotatedImage, str(i), face.upperLeft.exportCoordinates(), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


cv.imshow("After first projection and rotate", resizeMinTo500(rotatedImage))

# final faces coordinates

rotatedImage = rotateCounterClockwise(image, 0)

for i in range(len(DebugFaces)):
    (face, rotatedFaceOrigin, croppedCenter, rotatedImageCenter, relativeAngle, originalImageCenter)  = DebugFaces[i]
    face.projectArea(rotatedImageCenter, originalImageCenter)
    print("DEBUG OUT OF FUNCTION CHECK DIMENSIONS")
    print("biggestFaceOutOfFunction.dimensions", face.dimensions )
    print()

    face.draw(rotatedImage, (255, 255, 255), 2)
    cv.putText(rotatedImage, str(i), face.upperLeft.exportCoordinates(), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


cv.imshow("Final faces' coordinates", resizeMinTo500(rotatedImage))

cv.waitKey(0)


        
