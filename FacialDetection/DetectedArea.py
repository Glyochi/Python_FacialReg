import math
from FacialDetection import Point


class DetectedArea:
    """
    Object that stores the information of a rectangle encapsulates a detected object returned by cv.detectMultiscale(...).
    OpenCV returns 4-tuples (x,y,w,h) of rectangle marking down where the detected objects are. These information will be translated to many DetectedArea objects.
    DetectedArea will be used to compare with other DetectedArea.
    """
    def __init__(self, upperLeftPoint, angle, dimension, calibrated = False):
        """
        Construct a DetectedArea obj.
            @param upperLeftPoint (x,y): the 2-tuple coordinate of the upper left point of the rectangle encapsulates detected objects.
            @param angle: the angle of the image when the detected object was found and returned by openCV.
            @param dimension (w,h): the dimension of the box encapsulates the detected object.
            @param calibrated (True/False): whether the current 
        """
        self.upperLeftPoint = Point(upperLeftPoint[0], upperLeftPoint[1])
        self.angle = angle
        self.dimension = dimension
        self.centerPoint = Point(upperLeftPoint[0] + dimension[0]/2, upperLeftPoint[1] + dimension[1]/2)
        self.radius = math.sqrt(dimension[0]^2 + dimension[1]^2)
        self.calbirated = calibrated
    