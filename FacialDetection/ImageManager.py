import math
import cv2 as cv
import numpy as np
from numpy.lib.type_check import imag
from FacialDetection.Point import Point
from FacialDetection.DetectedArea import DetectedArea
from FacialDetection.rotate import rotate


""" 
    At this point in development, what I need the ImageManager to do is store the image, perform eyes detection on the image in 0, 90, 180, and 270 degree.
    
    Then ImageManager collects all "detected eyes" called DetectedArea objs, which still has the x, y cordinate corresponding to the rotated angle of the image when
    they were found. It then proceed to convert the x, y value to the cordinate in the original non-rotated image.
    
    After that, it checks for overlapping DetectedAreas and merge them into one big DetectedArea obj.

    Once that's done, we get an array of all the location of the eyes and their sizes. We can then connect every possible pair of approximately-same-size-eyes to see 
    if the distance between them are "reasonable". If a pair of eyes has a reasonable distance inbetweeen and the size of the eyes don't differ too much, 
    we can call it a potential face.

    Once we get an array of potential faces, we rotate the image by an angle decided by the position of the two eyes (to increase precision), crop out the face (to increase performance), 
    and run facial detection on that.

    At the end, ImageManger should have an array list of all detected faces.

"""
class ImageManager:
    """
    A manager that stores the actual image and can do image processing function on it. This object will be used to take care of facial detection.
    """
    haarcascade_eye = cv.CascadeClassifier("classifier/haarcascade_eye.xml")
    haarcascade_face = cv.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")
    def __init__(self, img):
        """
        Constructing an ImageManger object
            @param img: the image/frame that we will run facial detection on
        """
        # Blank canvas that we are going to use to store the rotated image
        self.img = img
        self.eyes = []
        self.faces = []
        self.imageCenter = (img.shape[0]/2, img.shape[1]/2)
    

    def runHaarDetection(self, haarDetection):
        """
        Run the given haarDetection on the image rotated by 0, 90, 180, 270 degree and return a 4-tuple of 4 arrays with corresponding angle that contain 
        detected objects (coordinates are relative to the center of the rotated image and are not yet translated to coordinates relative to
        the original non-rotated image)
            @return a 4-tuple of 4 arrays containing all the detected objects.
        """

    def mergeDetectedObjs(self, four_tuple):
        """
        Given a four-tuple containing 4 arrays of detected objects, scan through all of them and if find two duplicates (similar detected objects with similar 
        sizes and positions), merge them and put all the unique detected object in an array. 
            @return an array that contains all the unique detected objects.
        """
        (array0, array90, array180, array270) = four_tuple






    def findEyes(self):
        """
        Find the eyes in the image after applying haarcascade eye detection on the 0, 90, 180, and 270 degree rotated image. 
        Collect all the detected eyes and remove duplicates. 
            @return an array of detected eyes
        """
