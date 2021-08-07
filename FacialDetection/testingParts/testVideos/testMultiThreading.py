
import _thread
import threading
import time
import cv2 as cv
import sys
sys.path.append('FacialDetection')
from helperFunctions import *

haar_cascasde_eye = cv.CascadeClassifier("classifier/haarcascade_eye.xml")
haar_cascasde_nose = cv.CascadeClassifier("classifier/haarcascade_nose.xml")
haar_cascasde_face = cv.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")


# class testThread:
#     def __init__(self):
#         self.var = 0
        
#     def function1(self):
#         print()
#         print(f"new Frame {self.var}")
#         print()
        
#     def function2(self):
#         self.var = self.var + 1

#     def testMultiThread(self):
#         prev_frame = time.time()
#         timeFrame = 1/30
#         threads = []
#         for i in range(120):
#             if time.time() - prev_frame >= timeFrame:
#                 prev_frame = prev_frame + timeFrame
#                 threading.Thread(target=self.function1())

            

# a = testThread()
# a.testMultiThread()


"""
Multithreading doesnt really do much when applied to detectMultiScale since they are already parallelized
"""

class testThread:
    def __init__(self, dir):
        self.var = 0
        self.img = cv.imread(dir)
        self.grayImage = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        self.grayImage = resizeMinTo500(self.grayImage)
        
    def function1(self):
        haar_cascasde_face.detectMultiScale(self.grayImage, 1.2, 10)
        
    def function2(self):
        haar_cascasde_face.detectMultiScale(self.grayImage, 1.2, 10)

    def function3(self):
        haar_cascasde_face.detectMultiScale(self.grayImage, 1.2, 10)
        haar_cascasde_face.detectMultiScale(self.grayImage, 1.2, 10)

    def testMultiThread(self):
        try:
            threading.Thread(target= self.function1()).start()
            threading.Thread(target= self.function2()).start()
        except:
            print("Reeeee")
            

a = testThread("human/people.jpg")
a.function1()
startTime = time.time()
a.function1()
a.function2()
endTime = time.time()
print(f"Normal performance is       {endTime - startTime} seconds")
startTime = time.time()
t1 = threading.Thread(target= a.function1)
t2 = threading.Thread(target= a.function2)
t1.start()
t2.start()
t1.join()
t2.join()
endTime = time.time()
print(f"MultiThread performance is  {endTime - startTime} seconds")
startTime = time.time()
a.testMultiThread()
endTime = time.time()
print(f"MultiThread performance 2 is  {endTime - startTime} seconds")


# startTime = time.time()
# a.function1()
# endTime = time.time()
# print(f"Seperate run performance is        {endTime - startTime} seconds")

# startTime = time.time()
# t1 = threading.Thread(target = a.function1)
# t1.start()
# t2 = threading.Thread(target = a.function3)
# t2.start()
# t1.join()
# endTime = time.time()
# print(f"Multithreaded run performance is   {endTime - startTime} seconds")
# print(f"DEBUG t1 alive: {t1.is_alive()} t2 alive: {t2.is_alive()}")
# t2.join()
# endTime = time.time()
# print(f"Multithreaded run performance 2 is {endTime - startTime} seconds")
# print(f"DEBUG t1 alive: {t1.is_alive()} t2 alive: {t2.is_alive()}")




# a = testThread()
# a.testMultiThread(3, 1)
        
# class self:
#     def __init__(self):
#         self.var1 = 0
#         self.var2 = 0
# def function1(self, delay):
#     time.sleep(delay)
#     print(f"delay {delay} seconds")
#     self.var1 = self.var1 + 1
#     print(f"var1 {self.var1}")
#     print(f"var2 {self.var2}")
        
# def function2(self, delay):
#     time.sleep(delay)
#     print(f"delay {delay} seconds")
#     self.var2 = self.var2 + 1

# a = self()
# startTime = time.time()
# for i in range(0, 5):
#     try:
#         print(f"time {time.time() - startTime:0.2f}")
#         _thread.start_new_thread(function1, (a, 1))
#         time.sleep(1)
#         print(f"delay 1 seconds")
#         _thread.start_new_thread(function2, (a, 3))
#         time.sleep(1)
#         print(f"delay 1 seconds")
#         print("-----------------")
#     except:
#         print("ERROR testMultiThread")


# print(f"time {time.time() - startTime:0.2f}")
# print(f"var1 {a.var1}")
# print(f"var2 {a.var2}")

# while 1:
#     pass

