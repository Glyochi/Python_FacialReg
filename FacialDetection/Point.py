import math


class Point:
    """ 
    Point stores information of a point in an image and can calculate distance from itself to other Points.
    """
    def __init__(self, xCoord, yCoord, angle = 0):
        """ 
        Construct a point object.
            :param xCoord: the x coordinate.
            :param yCoord: the y coordinate.
        """
        self.x = xCoord
        self.y = yCoord

    def getX(self):
        """
        Return the point's x coordinate
            :return x coordinate
        """
        return self.x
        
    def getY(self):
        """
        Return the point's y coordinate
            :return y coordinate
        """
        return self.y

    def distTo(self, otherPoint):
        """
        Calculate the distance from the current point to the other point.
            :return the distance between two points.
        """
        distance = math.sqrt((self.x - otherPoint.x)**2 + (self.y - otherPoint.y)**2)
        return distance

    def rotatePointCounterClockwise(self, origin, angle):
        """
        Rotate the current point object by angle value counter-clockwise relative to the given origin.
            :param origin: the point where the function caller point object is going to rotate around
            :param angle: the angle the function caller point object is going to be rotated by
            :return the rotated point as a separated object
        """
        angle = angle % 360
        if angle == 0: 
            return Point(self.x, self.y)

        # print("DEBUG angle ", angle)
        # Calculating the relative angle to the origin
        dist = self.distTo(origin)
        deltaX = self.x - origin.x
        deltaY = self.y - origin.y
        if deltaX > 0:
            relativeAngle = (math.atan(deltaY/deltaX) * 180/math.pi + 360) % 360
        elif deltaX < 0:
            relativeAngle = math.atan(deltaY/deltaX) * 180/math.pi + 180
        elif deltaY > 0:
            # edge case when deltaX = 0, deltaY > 0
            relativeAngle = 90
        elif deltaY < 0:
            # edge case when deltaX = 0, deltaY < 0
            relativeAngle = 270
        else:
            # the point is the origin, no need to translate
            return Point(self.x, self.y)
        

        relativeAngle = (relativeAngle + angle + 360) % 360
        deltaX = math.cos(relativeAngle * math.pi / 180) * dist
        deltaY = math.sin(relativeAngle * math.pi / 180) * dist
        return Point(origin.x + deltaX, origin.y + deltaY)
        
    
    def rotatePointClockwise(self, origin, angle):
        """
        Translate the current point object by angle value clockwise relative to the given origin.
            :param origin: the point where the function caller point object is going to rotate around
            :param angle: the angle the function caller point object is going to be rotated by
            :return the rotatedPoint as a separated object
        """
        return self.rotatePointCounterClockwise(origin, -angle)

    def projectPoint(self, oldOrigin, newOrigin):
        """
        Calculate the position of a new point such that its position relative to newOrigin is the same as its 
        current relative position to old Origin.
        exp: current point is (1,1), oldOrigin is (0,0), and new origin is (2,0) => returned point is (3,1)
            :param oldOrigin: the old origin point
            :param newOrigin: the projected old Origin
            :return the projected current point such that its position relative to newOrigin is the same as current point to oldOrigin
        """

        projectedX = self.x + newOrigin.x - oldOrigin.x
        projectedY = self.y + newOrigin.y - oldOrigin.y
        return Point(projectedX, projectedY)