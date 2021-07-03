import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat3.jpg')

cv.imshow('Original', img)

blank = np.zeros(img.shape, dtype = 'uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscaled', gray)

# blurGray = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blurred + Grayscaled', blurGray)

canny = cv.Canny(gray, 125, 175)
cv.imshow('Canny Edges', canny)

# cv.threshold(...) binarize images. If a pixel brightness intensity is below 125, it will be set to 0 or black. If its above 125, it will be set to 1 or white
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Binarized', thresh)

# cv.RETR_LIST returns all the contours found in the image
# cv.RETR_EXTERNAL returns all the contours in the 'outside' found in the image
# cv.RETR_TREE returns all the hierarchial contours found in the image
# cv.CHAIN_APPROX_NONE means none filter we are getting all the contours found
# cv.CHAIN_APPROX_SIMPLE compress points of a contour of a straight line and returns the two end points only
contours, hierachies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

contoursDrawn = cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours drawn', contoursDrawn)

cv.waitKey(0)