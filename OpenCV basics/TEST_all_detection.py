import cv2 as cv
import math
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



haar_cascasde_left_EYE = cv.CascadeClassifier("classifier/haarcascade_lefteye.xml")
haar_cascasde_right_EYE = cv.CascadeClassifier("classifier/haarcascade_righteye.xml")
haar_cascasde_left_EAR = cv.CascadeClassifier("classifier/haarcascade_leftear.xml")
haar_cascasde_right_EAR = cv.CascadeClassifier("classifier/haarcascade_rightear.xml")
haar_cascasde_EYE = cv.CascadeClassifier("classifier/haarcascade_eye.xml")
haar_cascasde_nose = cv.CascadeClassifier("classifier/haarcascade_nose.xml")
haar_cascasde_face = cv.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")

font = cv.FONT_HERSHEY_SIMPLEX

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

    # frame = cv.resize(frame, (500, (int)(frame.shape[0] * 500 /frame.shape[1])))

    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Blue Green Red

    # Left Eye blue light (255, 255, 0)
    left_EYE_rect = haar_cascasde_left_EYE.detectMultiScale(grayFrame, scaleFactor = 1.1, minNeighbors=6, minSize = (30,30))
    for (x,y,w,h) in left_EYE_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255,255,0), thickness= 2)
        cv.putText(frame,'Left Eye blue light', (x, y - 5), font, 1, (255,255,0), 1)

    # Right Eye blue dark (255, 128, 0)
    right_EYE_rect = haar_cascasde_right_EYE.detectMultiScale(grayFrame, scaleFactor = 1.1, minNeighbors=6, minSize = (30,30))
    for (x,y,w,h) in right_EYE_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255,128,0), thickness= 2)
        cv.putText(frame,'Right Eye blue dark', (x, y -5), font, 1, (255,128,0), 1)

    # Eye blue darker (255, 0, 0)
    EYE_rect = haar_cascasde_EYE.detectMultiScale(grayFrame, scaleFactor = 1.1, minNeighbors=3, minSize = (30,30))
    for (x,y,w,h) in EYE_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255,0,0), thickness= 2)
        cv.putText(frame,'Eye blue darker', (x, y - 5), font, 1, (255,0,0), 2)

    # Nose Pink (255, 0, 255)
    # nose_rect = haar_cascasde_nose.detectMultiScale(grayFrame, scaleFactor = 1.1, minNeighbors=3, minSize = (30,30))
    # for (x,y,w,h) in nose_rect:
        # cv.rectangle(frame, (x, y), (x + w, y + h), (255,0,255), thickness= 2)
        # cv.putText(frame,'Nose pink', (x, y - 50), font, 1, (255,0,255), 2)

    # Left Ear yellow green (0, 255, 128)
    # left_EAR_rect = haar_cascasde_left_EAR.detectMultiScale(grayFrame, scaleFactor = 1.1, minNeighbors=3, minSize = (30,30))
    # for (x,y,w,h) in left_EAR_rect:
    #     cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 128), thickness= 2)
    #     cv.putText(frame,'Left Ear yellow green', (x, y - 50), font, 1, (0, 255, 128), 2)

    # Right Ear green (0, 255, 0)
    # right_EAR_rect = haar_cascasde_right_EAR.detectMultiScale(grayFrame, scaleFactor = 1.1, minNeighbors=3, minSize = (30,30))
    # for (x,y,w,h) in right_EAR_rect:
    #     cv.rectangle(frame, (x, y), (x + w, y + h), (255,128,0), thickness= 2)
    #     cv.putText(frame,'Right Ear green', (x, y - 50), font, 1, (255,128,0), 2)
        

    # Right Ear grey (160, 160, 160)
    # face_rect = haar_cascasde_face.detectMultiScale(grayFrame, scaleFactor = 1.1, minNeighbors=3, minSize = (30,30))
    # for (x,y,w,h) in face_rect:
    #     cv.rectangle(frame, (x, y), (x + w, y + h), (160, 160, 160), thickness= 2)
    #     cv.putText(frame,'Face grey', (x, y - 50), font, 1, (160, 160, 160), 2)

    cv.imshow('Video', frame)
    
    if cv.waitKey(1) & 0xFF == ord('d'):
        break


    

capture.release()
cv.destroyAllWindows()







# og = cv.resize(og, dimensions, interpolation=cv.INTER_AREA)

cv.waitKey(0)





