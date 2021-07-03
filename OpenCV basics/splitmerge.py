import cv2 as cv
import numpy as np

img = cv.imread('Photos/dog1.jpg')
cv.imshow('Original', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

b,g,r = cv.split(img)
#b,g,r are intensity maps of those 3 colors. The more white the pixel the more intensive the color is (blue/green/red)
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)


print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


merge = cv.merge([b,g,r])

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow('merge', merge)
cv.imshow('True blue', blue)
cv.imshow('True red', red)
cv.imshow('True green', green)

cv.waitKey(0)