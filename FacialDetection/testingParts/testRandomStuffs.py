
import cv2 as cv
import time
import sys
sys.path.append('FacialDetection')
from helperFunctions import *

haar_cascasde_eye = cv.CascadeClassifier("classifier/haarcascade_eye.xml")
haar_cascasde_nose = cv.CascadeClassifier("classifier/haarcascade_nose.xml")
haar_cascasde_face = cv.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")



img = cv.imread("human/people.jpg")
grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
grayImage = resizeMinTo500(grayImage)


print("Time window for a frame in a 24fps video is ", 1/24)


tic = time.perf_counter()
haar_cascasde_nose.detectMultiScale(grayImage, 2, 10, minSize = (30,30), maxSize = (100, 100))
toc = time.perf_counter()

print(f"Time taken to for nose detection 1:        {toc - tic:0.4f} seconds")

tic = time.perf_counter()
haar_cascasde_nose.detectMultiScale(grayImage, 1.2, 10, minSize = (30,30), maxSize = (100, 100))
toc = time.perf_counter()

print(f"Time taken to for nose detection 2:        {toc - tic:0.4f} seconds")

tic = time.perf_counter()
haar_cascasde_eye.detectMultiScale(grayImage, 1.2, 2, minSize = (30,30), maxSize = (100, 100))
toc = time.perf_counter()

print(f"Time taken to for eye detection:           {toc - tic:0.4f} seconds")

tic = time.perf_counter()
haar_cascasde_face.detectMultiScale(grayImage, 1.2, 10, minSize = (30,30), maxSize = (200, 200))
toc = time.perf_counter()

print(f"Time taken to for face detection:          {toc - tic:0.4f} seconds")





print("-----------------------------------------------------------------------")


img = cv.imread("human/people2.jpg")
grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
grayImage = resizeMinTo500(grayImage)


tic = time.perf_counter()
haar_cascasde_nose.detectMultiScale(grayImage, 2, 10, minSize = (30,30), maxSize = (100, 100))
toc = time.perf_counter()

print(f"Time taken to for nose detection 1:        {toc - tic:0.4f} seconds")

tic = time.perf_counter()
haar_cascasde_nose.detectMultiScale(grayImage, 1.2, 10, minSize = (30,30), maxSize = (100, 100))
toc = time.perf_counter()

print(f"Time taken to for nose detection 2:        {toc - tic:0.4f} seconds")

tic = time.perf_counter()
haar_cascasde_eye.detectMultiScale(grayImage, 1.2, 2, minSize = (30,30), maxSize = (100, 100))
toc = time.perf_counter()

print(f"Time taken to for eye detection:           {toc - tic:0.4f} seconds")

tic = time.perf_counter()
haar_cascasde_face.detectMultiScale(grayImage, 1.2, 10, minSize = (30,30), maxSize = (200, 200))
toc = time.perf_counter()

print(f"Time taken to for face detection:          {toc - tic:0.4f} seconds")