import cv2 as cv

img = cv.imread('Photos/cat1.jpg')
cv.imshow('Original', img)


# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# Grayscale to BGR
bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('recreated BGR', bgr)

# # BGR to HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)


# # BGR to LAB (L+a+b)
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)


# # BGR to RGB
# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB', rgb)
cv.waitKey(0)