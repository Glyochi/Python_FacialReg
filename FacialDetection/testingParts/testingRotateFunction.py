import math
import cv2 as cv
import numpy as np
from numpy.core.fromnumeric import shape

img = cv.imread("human/people.jpg")
# cv.imshow("OG", img)

# rescale an image/frame
def rescaleFrame(frame, newWidth):
    width = newWidth
    height = (int)(frame.shape[0] * newWidth / frame.shape[1])
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    # Calculating the dimension of the new canvas to store the entire rotated image without cropping, 
    # diagAngleA is half the angle of the lowest angle created by the two diagonals. diagAngleB is half the angle of the rightest angle created by the two diagonals.
    diagLen = math.sqrt(width**2 + height**2)
    diagAngleA = math.atan(width/height)
    diagAngleB = math.pi/2 - diagAngleA
    print("Debug diagLen", diagLen)
    print("Debug angleA", diagAngleA*180/math.pi)
    print("Debug angleB", diagAngleB*180/math.pi)

    # TempAngle is used to keep the angle value in math.cos stays between -90 and 90 degree => consistence cos value 
    # cos value is the cosine of the offset of frame/img diagonal line from the x/y axis (diagAngle + tempAngle*math.pi/180 - math.pi/2). 
    # And using the value of angle, we will know which cos value is used to determined width and height.
    # angle < 360 to avoid edge cases
    angle = angle % 360
    print("Debug negative angle", angle)
    tempAngle = angle%90
    if (angle >= 0 and angle < 90) or (angle >= 180 and angle < 270):
        
        fittingWidth = math.floor(math.cos(diagAngleA + tempAngle*math.pi/180 - math.pi/2) * diagLen)
        fittingHeight = math.floor(math.cos(diagAngleB + tempAngle*math.pi/180 - math.pi/2) * diagLen)
    else :
        fittingWidth = math.floor(math.cos(diagAngleB + tempAngle*math.pi/180 - math.pi/2) * diagLen)
        fittingHeight = math.floor(math.cos(diagAngleA + tempAngle*math.pi/180 - math.pi/2) * diagLen)

    # Drawing pre rotated image ontop of bigger canvas
    # rotatedCanvas initially takes the largest horizontal/vertical value among newWidth, newHeight, img.shape[1], img.shape[2] to prevent the image from cropping and index out of bound
    # Once the image is rotated on rotatedCanvas, we will crop out the excess part
    rotatedCanvas = np.zeros((max(fittingHeight, img.shape[0]), max(fittingWidth, img.shape[1]), 3), dtype='uint8')
    rotatedCanvas[math.floor(rotatedCanvas.shape[0]/2 - img.shape[0]/2): math.floor(rotatedCanvas.shape[0]/2 + img.shape[0]/2), math.floor(rotatedCanvas.shape[1]/2 - img.shape[1]/2): math.floor(rotatedCanvas.shape[1]/2 + img.shape[1]/2)] = img
    # rotatedCanvas[100:200,400:500] = 0,255,0
    # [upper height bound: lower height bound, left width bound: right width bound]
    # cv.imshow("Test draw on cavnas before rotate", rescaleFrame(rotatedCanvas, 500))

    #rotPoint (width, height)
    if rotPoint is None:
        rotPoint = (rotatedCanvas.shape[1]//2, rotatedCanvas.shape[0]//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    excessDimensions = (rotatedCanvas.shape[1], rotatedCanvas.shape[0])
    rotatedCanvas = cv.warpAffine(rotatedCanvas, rotMat, excessDimensions)
    cv.imshow("Rotated not crop out excess", rescaleFrame(rotatedCanvas, 500))
    # rotatedCanvas = rotatedCanvas[100:1200, 100:600]
    # Cropping excess borders
    rotatedCanvas = rotatedCanvas[math.floor((rotatedCanvas.shape[0] - fittingHeight)/2) : math.floor((rotatedCanvas.shape[0] + fittingHeight)/2), math.floor((rotatedCanvas.shape[1] - fittingWidth)/2) : math.floor((rotatedCanvas.shape[1] + fittingWidth)/2)]
    print("Debug fitting height", fittingHeight)
    print("Debug fitting width", fittingWidth)
    print("Debug upper height bound", math.floor((rotatedCanvas.shape[0] - fittingHeight)/2))
    print("Debug lower height bound", math.floor((rotatedCanvas.shape[0] + fittingHeight)/2))
    print("Debug left width bound", math.floor((rotatedCanvas.shape[1] - fittingWidth)/2))
    print("Debug right width bound", math.floor((rotatedCanvas.shape[1] + fittingWidth)/2))
    return rotatedCanvas

blank = rotate(img,-60)
for x in range(0, 360, 10):
    blank = rotate(img, x)
    blank = rescaleFrame(blank, 500)
    cv.imshow('Rotated' + str(x) + 'degree', blank)






cv.waitKey(0)