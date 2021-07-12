from Point import Point


class DetectedArea:
    """
    Object that stores the center of a rectangle encapsulates a detected object returned by cv.detectMultiscale(...), 
    the angle of the image when it was detected, and the dimensions of the rectangle.
    OpenCV returns 4-tuples (x,y,w,h) of rectangle marking down where the detected objects are. These information will be translated to many DetectedArea objects.
    DetectedArea will be used to compare with other DetectedArea.
    """
    def __init__(self, upperLeftPoint, dimensions):
        """
        Construct a DetectedArea obj.
            @param upperLeftPoint (x,y): the 2-tuple coordinates of the upper left point of the rectangle encapsulates detected objects.
            @param angle: the angle of the image when the detected object was found and returned by openCV.
            @param dimension (w,h): the dimension of the box encapsulates the detected object.
        """
        self.dimensions = dimensions
        self.upperLeft = Point(upperLeftPoint[0], upperLeftPoint[1])
        self.center = Point(upperLeftPoint[0] + dimensions[0]/2, upperLeftPoint[1] + dimensions[1]/2)
    
    def rotateAreaCounterClockwise(self, origin, angle):
        """
        Rotate the detectedArea object counter-clockwise around an origin by a given degree.
            @param origin: the point where detectedArea is going to rotate around
            @param angle: the angle the detectedArea is going to rotate by
        """
        self.upperLeft.rotatePointCounterClockwise(origin, angle)
        self.center.rotatePointCounterClockwise(origin, angle)

    def rotateAreaClockwise(self, origin, angle):
        """
        Rotate the detectedArea object clockwise around an origin by a given degree.
            @param origin: the point where detectedArea is going to rotate around
            @param angle: the angle the detectedArea is going to rotate by
        """
        self.upperLeft.rotatePointClockwise(origin, angle)
        self.center.rotatePointClockwise(origin, angle)
        
    def projectRectangle(self, oldOrigin, newOrigin):
        """
        Project the rectangle such that its new position relative to newOrigin is 
        the same as its current relative position to oldOrigin.
            @param oldOrigin: the old origin point
            @param newOrigin: the projected old Origin
        """
        self.center = self.center.projectPoint(oldOrigin, newOrigin)
        self.upperLeft = self.upperLeft.projectPoint(oldOrigin, newOrigin)

    def overlap(self, otherArea):
        """
        Check for overlap between two detectedAreas. (NOT FINALIZED CONDITION PARAMETERS)
            @param otherArea: the DetectedArea that we are going to check for overlap
            @return True/False
        """
        print("DetectedArea overlap: NOT FINALIZED CONDITION PARAMETERS")
        distance = self.center.distTo(otherArea.center)
        if distance < (self.center.distTo(self.upperLeft) + otherArea.center.distTo(otherArea.upperLeft))/2:
            return True
        return False
    
    def similarSize(self, otherArea):
        """
        Compare the size with another area to see if the two DetectedAreas are similar. (NOT FINALIZED CONDITION PARAMETERS)
            @param otherArea: the DetectedArea that we are comparing to
            @return True/False
        """
        print("DetectedArea similarSize: NOT FINALIZED CONDITION PARAMETERS")
        thisSize = self.center.distTo(self.upperLeft)
        otherSize = otherArea.center.distTo(otherArea.upperLeft)

        minSize = min(thisSize, otherSize)
        maxSize = max(thisSize, otherSize)

        if min > max * 0.7:
            return True
        return False

    def merge(self, otherArea):
        """
        Merge another area into itself to make a bigger area. This does not delete the other area object. (NOT FINALIZED CONDITION PARAMETERS)
            @param otherArea: the DetectedArea that we are merging with
        """
        print("DetectedArea merge: NOT FINALIZED CONDITION PARAMETERS")
        # For right now, we just use the bigger area
        
        thisSize = self.center.distTo(self.upperLeft)
        otherSize = otherArea.center.distTo(otherArea.upperLeft)
        if otherSize > thisSize:
            self.center = otherArea.center
            self.upperLeft = otherArea.upperLeft
            self.dimensions = otherArea.dimensions
        



