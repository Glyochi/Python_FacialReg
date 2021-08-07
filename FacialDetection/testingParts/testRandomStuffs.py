
import cv2 as cv
import time
import sys
sys.path.append('FacialDetection')
from helperFunctions import *
# include <opencv2/core/core.hpp>
# define SIMD_OPENCV_ENABLE
# include "Simd/SimdLib.hpp"

img = cv.imread("human/people.jpg")
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
oldFaceDetector = cv.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")
# newFaceDetector = cv.CascadeClassifier("classifier/lbpcascade_frontalface_improved.xml")
newFaceDetector = cv.CascadeClassifier("classifier/lbpcascaade_frontalface_improved.xml")

start = time.time()
oldFaceDetector.detectMultiScale(grayImg, 1.1, 10)
print(f"Old detection run time {time.time() - start}")

start = time.time()
newFaceDetector.detectMultiScale(grayImg, 1.1, 10)
print(f"Old detection run time {time.time() - start}")








# img = cv.imread("human/people.jpg")

# start = time.time()
# resizedImage = TEST_INTERPOLATION_TYPE_resizeMinTo(img, 500, 0)
# print(f"DEBUG INTER_AREA runtime:     {time.time() - start}")

# start = time.time()
# resizedImage = TEST_INTERPOLATION_TYPE_resizeMinTo(img, 500, 0)
# print(f"DEBUG INTER_AREA runtime:     {time.time() - start}")

# start = time.time()
# resizedImage = TEST_INTERPOLATION_TYPE_resizeMinTo(img, 500, 1)
# print(f"DEBUG INTER_CUBIC runtime:    {time.time() - start}")

# start = time.time()
# resizedImage = TEST_INTERPOLATION_TYPE_resizeMinTo(img, 500, 2)
# print(f"DEBUG INTER_LANCZOS4 runtime: {time.time() - start}")

# start = time.time()
# resizedImage = TEST_INTERPOLATION_TYPE_resizeMinTo(img, 500, 3)
# print(f"DEBUG INTER_NEAREST runtime:  {time.time() - start}")

# start = time.time()
# resizedImage = TEST_INTERPOLATION_TYPE_resizeMinTo(img, 500, 4)
# print(f"DEBUG INTER_LINEAR runtime:   {time.time() - start}")


# print("---------------------------------------------")
# img = cv.imread("human/people2.jpg")
# img = cv.imread("human/people.jpg")

# start = time.time()
# resizedImage = TEST_INTERPOLATION_TYPE_resizeMinTo(img, 500, 0)
# print(f"DEBUG INTER_AREA runtime:     {time.time() - start}")

# start = time.time()
# resizedImage = TEST_INTERPOLATION_TYPE_resizeMinTo(img, 500, 0)
# print(f"DEBUG INTER_AREA runtime:     {time.time() - start}")

# start = time.time()
# resizedImage = TEST_INTERPOLATION_TYPE_resizeMinTo(img, 500, 1)
# print(f"DEBUG INTER_CUBIC runtime:    {time.time() - start}")

# start = time.time()
# resizedImage = TEST_INTERPOLATION_TYPE_resizeMinTo(img, 500, 2)
# print(f"DEBUG INTER_LANCZOS4 runtime: {time.time() - start}")

# start = time.time()
# resizedImage = TEST_INTERPOLATION_TYPE_resizeMinTo(img, 500, 3)
# print(f"DEBUG INTER_NEAREST runtime:  {time.time() - start}")

# start = time.time()
# resizedImage = TEST_INTERPOLATION_TYPE_resizeMinTo(img, 500, 4)
# print(f"DEBUG INTER_LINEAR runtime:   {time.time() - start}")








# class object:
#     def __init__(self, number):
#         self.number = number
# a = object(1)
# b = object(2)
# c = object(3)
# d = object(4)
# array = [a,b,c,d]

# int = 4
# for element in array:
#     element = object(int)
#     int = int - 1
# for element in array:
#     print(f"DEBUG {element.number}")


# haar_cascasde_eye = cv.CascadeClassifier("classifier/haarcascade_eye.xml")
# haar_cascasde_nose = cv.CascadeClassifier("classifier/haarcascade_nose.xml")
# haar_cascasde_face = cv.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")



# img = cv.imread("human/people.jpg")
# grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# grayImage = resizeMinTo500(grayImage)


# print("Time window for a frame in a 24fps video is ", 1/15)


# tic = time.perf_counter()
# haar_cascasde_nose.detectMultiScale(grayImage, 2, 10, minSize = (30,30), maxSize = (100, 100))
# toc = time.perf_counter()

# print(f"Time taken to for nose detection 1:        {toc - tic:0.4f} seconds")

# tic = time.perf_counter()
# haar_cascasde_nose.detectMultiScale(grayImage, 1.2, 10)
# toc = time.perf_counter()

# print(f"Time taken to for nose detection 2:        {toc - tic:0.4f} seconds")

# tic = time.perf_counter()
# haar_cascasde_eye.detectMultiScale(grayImage, 1.2, 2)
# toc = time.perf_counter()

# print(f"Time taken to for eye detection:           {toc - tic:0.4f} seconds")

# tic = time.perf_counter()
# haar_cascasde_face.detectMultiScale(grayImage, 1.2, 10)
# toc = time.perf_counter()

# print(f"Time taken to for face detection:          {toc - tic:0.4f} seconds")





# print("-----------------------------------------------------------------------")


# img = cv.imread("human/people2.jpg")
# grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# grayImage = resizeMinTo500(grayImage)


# tic = time.perf_counter()
# haar_cascasde_nose.detectMultiScale(grayImage, 2, 10, minSize = (30,30), maxSize = (100, 100))
# toc = time.perf_counter()

# print(f"Time taken to for nose detection 1:        {toc - tic:0.4f} seconds")

# tic = time.perf_counter()
# haar_cascasde_nose.detectMultiScale(grayImage, 1.2, 10)
# toc = time.perf_counter()

# print(f"Time taken to for nose detection:          {toc - tic:0.4f} seconds")

# tic = time.perf_counter()
# haar_cascasde_eye.detectMultiScale(grayImage, 1.2, 10)
# toc = time.perf_counter()

# print(f"Time taken to for eye detection:           {toc - tic:0.4f} seconds")

# tic = time.perf_counter()
# haar_cascasde_face.detectMultiScale(grayImage, 1.2, 10)
# toc = time.perf_counter()

# print(f"Time taken to for face detection:          {toc - tic:0.4f} seconds")

