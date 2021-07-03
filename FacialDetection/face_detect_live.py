import cv2 as cv
import math
from datetime import datetime
import numpy as np

# Functions ---- Functions ---- Functions ---- Functions ---- Functions ---- Functions ---- Functions ---- Functions

# Shit rotates positive angle counter clockwise, negative angle clockwise
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)



# Functions ---- Functions ---- Functions ---- Functions ---- Functions ---- Functions ---- Functions ---- Functions



haar_cascasde_eye = cv.CascadeClassifier("classifier/haarcascade_eye.xml")
haar_cascasde_face = cv.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")

# x is horizontal, y is vertical

capture = cv.VideoCapture('http://192.168.1.17:8080/video')

# diagonal_len = math.sqrt(capture.shape[0]^2 + capture.shape[1]^2)
# rotated_grayFrame = np.zeros((diagonal_len,diagonal_len), dtype = 'uint8')
# rotated_grayFrame = (rotated_grayFrame.shape[0]/2, rotated_grayFrame.shape[1]/2)
# frame_center = (capture.shape[0]/2 , capture.shape[1]/2)


# Reading frames from capture and grayscaling those frame, find the eyes, draw the line for every pair of eyes and rotate the image so that that line is horizontally.
# For each pair of eyes, crop the "potential face match" then pass that cropped frame into haar_cascade_face.detectMultiScale to check if its a face. Save the coordinate
# and the size of the face and draw boxes around all faces onto the original frame when all pairs of eyes are tested.

while True:
    isTrue, frame = capture.read()

    frame = cv.resize(frame, (500, (int)(frame.shape[0] * 500 /frame.shape[1])))

    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    eyes_detected = haar_cascasde_eye.detectMultiScale(grayFrame, scaleFactor = 1.1, minNeighbors = 6, flags = cv.CASCADE_SCALE_IMAGE)

    i = 0
    while i < len(eyes_detected) - 1:
        y = i + 1
        while y <len(eyes_detected):
            # (x,y,w,h)
            # Locating the pair of eyes' centers
            first_eye = (eyes_detected[i][0] + eyes_detected[i][2]/2, eyes_detected[i][1] + eyes_detected[i][3]/2)
            second_eye = (eyes_detected[y][0] + + eyes_detected[y][2]/2, eyes_detected[y][1] + eyes_detected[y][3]/2)

            # Calculating angles and distance between the twos
            vertical_dif = second_eye[0] - first_eye[0]
            horizontal_dif = second_eye[1] - first_eye[1]
            angle = math.atan((vertical_dif/horizontal_dif) * 180 / math.pi) 
            distance = math.sqrt(vertical_dif^2 + horizontal_dif^2)

            # Rotate the image, calculate new coordinate and crop out the potential face match
            rotated_grayFrame = rotate(grayFrame, 0 - angle, frame_center) #invert angle cause u want the eye-line to be horizontal



        

    faces_rect = haar_cascasde_face.detectMultiScale(grayFrame, scaleFactor = 1.1, minNeighbors=6, minSize = (30,30), flags=cv.CASCADE_SCALE_IMAGE)

    

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), thickness= 2)

    cv.imshow('Video', frame)
    
    if cv.waitKey(1) & 0xFF == ord('d'):
        break


    

capture.release()
cv.destroyAllWindows()







# og = cv.resize(og, dimensions, interpolation=cv.INTER_AREA)

cv.waitKey(0)





