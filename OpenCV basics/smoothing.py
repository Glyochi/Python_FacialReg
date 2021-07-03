import cv2 as cv
import numpy as np


img = cv.imread('Photos/Cat1.jpg')
cv.imshow('Orginal', img)

# Averaging, Gaussian, and Median blur using the values in a kernel (a window with the blurring pixel at the center)
# Bilateral use a radius

# Averaging
average =  cv.blur(img, (3,3))
cv.imshow('Average blur', average)


# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median blur', median)

# Bilateral /remove noises?
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)





cv.waitKey(0)