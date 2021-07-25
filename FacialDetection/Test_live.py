from helperFunctions import resizeToMin500
import cv2 as cv
import math
from datetime import datetime
import numpy as np
import sys
sys.path.append('FacialDetection')
from ImageManager import ImageManager

#


haar_cascasde_eye = cv.CascadeClassifier("classifier/haarcascade_eye.xml")
haar_cascasde_face = cv.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")

# x is horizontal, y is vertical

capture = cv.VideoCapture('http://192.168.1.17:8080/video')


# Reading frames from capture and grayscaling those frame, find the eyes, draw the line for every pair of eyes and rotate the image so that that line is horizontally.
# For each pair of eyes, crop the "potential face match" then pass that cropped frame into haar_cascade_face.detectMultiScale to check if its a face. Save the coordinate
# and the size of the face and draw boxes around all faces onto the original frame when all pairs of eyes are tested.

while True:
    isTrue, frame = capture.read()

    resizeToMin500(frame)

    imgMgnr = ImageManager(frame)

    imgMgnr.findPairsOfEyes(1.2, 10)

    

    for eye in imgMgnr.eyes:
        eye.draw(frame,(0,255,0), 2)

    cv.imshow('Video', frame)
    
    if cv.waitKey(1) & 0xFF == ord('d'):
        break


    

capture.release()
cv.destroyAllWindows()







# og = cv.resize(og, dimensions, interpolation=cv.INTER_AREA)

cv.waitKey(0)





