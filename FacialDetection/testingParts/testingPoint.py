import math

class Point:
    """ 
    Point stores information of a point in an image and can calculate distance from itself to other Points.
    """
    def __init__(self, xCoord, yCoord, angle = 0):
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
        distance = math.sqrt((self.x - otherPoint.x)**2 + (self.y - otherPoint.y)**2)
        return distance

    

    def translateByAngleCounterClockwise(self, origin, angle):
        """
        Translate the current point object by angle value clockwise relative to the given origin.
        """
        angle = angle % 360
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
            return
        
        # print("DEBUG deltaX ", deltaX)
        # print("DEBUG deltaY ", deltaY)
        # print("DEBUG relativeAngle ", relativeAngle)

        relativeAngle = (relativeAngle + angle + 360) % 360
        deltaX = math.cos(relativeAngle * math.pi / 180) * dist
        deltaY = math.sin(relativeAngle * math.pi / 180) * dist
        self.x = origin.x + deltaX
        self.y = origin.y + deltaY
        # print("DEBUG new deltaX ", deltaX)
        # print("DEBUG new deltaY ", deltaY)
        # print("DEBUG newX ", self.x)
        # print("DEBUG newY ", self.y)
        # print("DEBUG relativeAngle ", relativeAngle)

    import math

class Point:
    """ 
    Point stores information of a point in an image and can calculate distance from itself to other Points.
    """
    def __init__(self, xCoord, yCoord, angle = 0):
        """ 
        Construct a point object.
            @param xCoord: the x coordinate.
            @param yCoord: the y coordinate.
        """
        self.x = xCoord
        self.y = yCoord

    def getX(self):
        """
        Return the point's x coordinate
            @return x coordinate
        """
        return self.x
        
    def getY(self):
        """
        Return the point's y coordinate
            @return y coordinate
        """
        return self.y

    def distTo(self, otherPoint):
        """
        Calculate the distance from the current point to the other point.
            @return the distance between two points.
        """
        distance = math.sqrt((self.x - otherPoint.x)**2 + (self.y - otherPoint.y)**2)
        return distance

    def translateByAngleCounterClockwise(self, origin, angle):
        """
        Rotate the current point object by angle value counter-clockwise relative to the given origin.
            @param origin: the point where the function caller point object is going to rotate around
            @param angle: the angle the function caller point object is going to be rotated by
            @return none
        """
        angle = angle % 360
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
            return
        

        relativeAngle = (relativeAngle + angle + 360) % 360
        deltaX = math.cos(relativeAngle * math.pi / 180) * dist
        deltaY = math.sin(relativeAngle * math.pi / 180) * dist
        self.x = origin.x + deltaX
        self.y = origin.y + deltaY

    
    def translateByAngleClockwise(self, origin, angle):
        """
        Translate the current point object by angle value clockwise relative to the given origin.
            @param origin: the point where the function caller point object is going to rotate around
            @param angle: the angle the function caller point object is going to be rotated by
            @return none
        """
        self.translateByAngleCounterClockwise(origin, -angle)
