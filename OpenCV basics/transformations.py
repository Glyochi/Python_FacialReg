import cv2 as cv
import numpy as np

img = cv.imread('Photos/dog1.jpg')

cv.imshow('Dog1', img)

# Translate (repositioning)
# def translate(img, x, y):
#     transMat = np.float32(([1,0,x],[0,1,y]))
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, transMat, dimensions)

# # -x --> left
# # +x --> right
# # -y --> up
# # +y --> down

# translated = translate(img, -100, 100)
# cv.imshow('Translated Dog1', translated)




# Rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated dog1', rotated)





# Resizing
# resized = cv.resize(img, (500, 100), interpolation= cv.INTER_CUBIC)
# cv.imshow('Resized dog1', resized)



# Flipping
# 0 = flipping vertically
# 0 = flipping horizontally
# 0 = flipping both ways
# flip = cv.flip(img, 0)
# cv.imshow('Flipped Dog1', flip)



# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped Dog1', cropped)

cv.waitKey(0)
