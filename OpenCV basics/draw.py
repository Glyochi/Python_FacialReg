import cv2 as cv
import numpy as np

# create a blank image
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
blank[200:300, 300:400] = 0, 255, 0
cv.imshow('Greennnn', blank)
blank[100:200, 50:250] = 255, 0, 0
cv.imshow('Blue', blank)


blank[:] = 0, 0, 0

# 2. Draw a Rectangle

# #thickness 2
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness= 2)
# #filled rectangle
# # cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness= -1)
# #filled rectangle -1 = cv.FILLED
# # cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness= -cv.FILLED)
# cv.imshow('Rectangle', blank)


# 3. Draw a Circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (255,0,0), thickness = 3)
# cv.imshow('Circle', blank)


# 4. Draw a line
# cv.line(blank, (0, 0),
#         (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=5)
# cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)

while not cv.waitKey(0):
    69420

cv.destroyAllWindows()
