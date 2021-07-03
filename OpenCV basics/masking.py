import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat1.jpg')
cv.imshow('Cats', img)


blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

mask_area = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 500, 255, -1)
cv.imshow('Mask', mask_area)

masked = cv.bitwise_and(img, img, mask= mask_area)
cv.imshow('Masked image', masked)


cv.waitKey(0)