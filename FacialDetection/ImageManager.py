import math
import cv2 as cv
import numpy as np
from numpy.lib.type_check import imag
from FacialDetection.Point import Point
from FacialDetection.DetectedArea import DetectedArea
from FacialDetection.rotate import rotate


class ImageManager:
    """
    A manager that stores the actual image and can do image processing function on it. This object will be used to take care of facial detection.
    """
    haarcascade_eye = cv.CascadeClassifier("classifier/haarcascade_eye.xml")

    def __init__(self, img):
        """
        Constructing an ImageManger object
            @param img: the image/frame that we will run facial detection on
        """
        # Blank canvas that we are going to use to store the rotated image
        self.img = img
    

