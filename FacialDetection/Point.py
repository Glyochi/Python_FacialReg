import math

class Point:
    """ 
    Point stores information of a point in an image and can calculate distance from itself to other Points.
    """
    def __init__(self, xCoord, yCoord, angle):
        """ 
        Construct a point object.
            @param xCoord: the x coordinate.
            @param yCoord: the y coordinate.
        """
        self.x = xCoord
        self.y = yCoord

    def distTo(self, otherPoint):
        """
        Calculate the distance from the current point to the other point.
            @return the distance between two points.
        """
        distance = math.sqrt((self.x - otherPoint.x)^2 + (self.y - otherPoint.y)^2)
        return distance

