import unittest
from math import sqrt
from FacialDetection.Point import Point

class TestPointMethods(unittest.TestCase):
    def test_translateByAngleCounterClockwise_90(self):        
        #Check rotate by 90 degree
        
        msg = "Rotated by 90 degree counter-clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a.translateByAngleCounterClockwise(b, 90)
        self.assertAlmostEqual(-1, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a.translateByAngleCounterClockwise(b, 90)
        self.assertAlmostEqual(2, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg + " " + case + ": y coordinate is wrong")


    def test_translateByAngleCounterClockwise_180(self):  
        #Check rotate by 180 degree
        
        msg = "Rotated by 180 degree counter-clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a.translateByAngleCounterClockwise(b, 180)
        self.assertAlmostEqual(-1, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(-1, a.y, 8, msg + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a.translateByAngleCounterClockwise(b, 180)
        self.assertAlmostEqual(2, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(2, a.y, 8, msg + " " + case + ": y coordinate is wrong")

 
    def test_translateByAngleCounterClockwise_270(self):        
        #Check rotate by 270 degree
        
        msg = "Rotated by 270 degree counter-clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a.translateByAngleCounterClockwise(b, 270)
        self.assertAlmostEqual(1, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(-1, a.y, 8, msg + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a.translateByAngleCounterClockwise(b, 270)
        self.assertAlmostEqual(4, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(2, a.y, 8, msg + " " + case + ": y coordinate is wrong")   
       
   
    def test_translateByAngleCounterClockwise_360(self):      
        #Check rotate by 360 degree

        msg = "Rotated by 360 degree counter-clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)

        a.translateByAngleCounterClockwise(b, 360)
        self.assertAlmostEqual(1, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)

        a.translateByAngleCounterClockwise(b, 360)
        self.assertAlmostEqual(4, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg + " " + case + ": y coordinate is wrong")       


#########################################################################################################################
#########################################################################################################################


    def test_translateByAngleCounterClockwise_45(self):        
        #Check rotate by 45 degree
        
        msg = "Rotated by 45 degree counter-clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a.translateByAngleCounterClockwise(b, 45)
        self.assertAlmostEqual(0, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(sqrt(2), a.y, 8, msg + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a.translateByAngleCounterClockwise(b, 45)
        self.assertAlmostEqual(3, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(3 + sqrt(2), a.y, 8, msg + " " + case + ": y coordinate is wrong")


    def test_translateByAngleCounterClockwise_135(self):  
        #Check rotate by 135 degree
        
        msg = "Rotated by 135 degree counter-clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a.translateByAngleCounterClockwise(b, 135)
        self.assertAlmostEqual(-sqrt(2), a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(0, a.y, 8, msg + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a.translateByAngleCounterClockwise(b, 135)
        self.assertAlmostEqual(3 - sqrt(2), a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(3, a.y, 8, msg + " " + case + ": y coordinate is wrong")

 
    def test_translateByAngleCounterClockwise_225(self):        
        #Check rotate by 225 degree
        
        msg = "Rotated by 225 degree counter-clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a.translateByAngleCounterClockwise(b, 225)
        self.assertAlmostEqual(0, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(-sqrt(2), a.y, 8, msg + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a.translateByAngleCounterClockwise(b, 225)
        self.assertAlmostEqual(3, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(3 - sqrt(2), a.y, 8, msg + " " + case + ": y coordinate is wrong")   
       
   
    def test_translateByAngleCounterClockwise_315(self):      
        #Check rotate by 315 degree

        msg = "Rotated by 315 degree counter-clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)

        a.translateByAngleCounterClockwise(b, 315)
        self.assertAlmostEqual(sqrt(2), a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(0, a.y, 8, msg + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)

        a.translateByAngleCounterClockwise(b, 315)
        self.assertAlmostEqual(3 + sqrt(2), a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(3, a.y, 8, msg + " " + case + ": y coordinate is wrong")       



#########################################################################################################################
#########################################################################################################################

        
    def test_translateByAngleCounterClockwise_neg90(self):        
        #Check rotate by -90 degree
        
        msg = "Rotated by -90 degree counter-clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a.translateByAngleCounterClockwise(b, -90)
        self.assertAlmostEqual(1, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(-1, a.y, 8, msg + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a.translateByAngleCounterClockwise(b, -90)
        self.assertAlmostEqual(4, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(2, a.y, 8, msg + " " + case + ": y coordinate is wrong")


    def test_translateByAngleCounterClockwise_neg180(self):  
        #Check rotate by -180 degree
        
        msg = "Rotated by -180 degree counter-clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a.translateByAngleCounterClockwise(b, -180)
        self.assertAlmostEqual(-1, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(-1, a.y, 8, msg + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a.translateByAngleCounterClockwise(b, -180)
        self.assertAlmostEqual(2, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(2, a.y, 8, msg + " " + case + ": y coordinate is wrong")

 
    def test_translateByAngleCounterClockwise_neg270(self):        
        #Check rotate by -270 degree
        
        msg = "Rotated by -270 degree counter-clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a.translateByAngleCounterClockwise(b, -270)
        self.assertAlmostEqual(-1, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a.translateByAngleCounterClockwise(b, -270)
        self.assertAlmostEqual(2, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg + " " + case + ": y coordinate is wrong")   
       
   
    def test_translateByAngleCounterClockwise_neg360(self):      
        #Check rotate by -360 degree

        msg = "Rotated by -360 degree counter-clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)

        a.translateByAngleCounterClockwise(b, -360)
        self.assertAlmostEqual(1, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)

        a.translateByAngleCounterClockwise(b, -360)
        self.assertAlmostEqual(4, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg + " " + case + ": y coordinate is wrong")       


#########################################################################################################################
#########################################################################################################################


    def test_translateByAngleCounterClockwise_neg45(self):        
        #Check rotate by -45 degree
        
        msg = "Rotated by -45 degree counter-clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a.translateByAngleCounterClockwise(b, -45)
        self.assertAlmostEqual(sqrt(2), a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(0, a.y, 8, msg + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a.translateByAngleCounterClockwise(b, -45)
        self.assertAlmostEqual(3 + sqrt(2), a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(3, a.y, 8, msg + " " + case + ": y coordinate is wrong")


    def test_translateByAngleCounterClockwise_neg135(self):  
        #Check rotate by -135 degree
        
        msg = "Rotated by -135 degree counter-clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a.translateByAngleCounterClockwise(b, -135)
        self.assertAlmostEqual(0, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(-sqrt(2), a.y, 8, msg + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a.translateByAngleCounterClockwise(b, -135)
        self.assertAlmostEqual(3, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(3 - sqrt(2), a.y, 8, msg + " " + case + ": y coordinate is wrong")

 
    def test_translateByAngleCounterClockwise_neg225(self):        
        #Check rotate by -225 degree
        
        msg = "Rotated by -225 degree counter-clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a.translateByAngleCounterClockwise(b, -225)
        self.assertAlmostEqual(-sqrt(2), a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(0, a.y, 8, msg + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a.translateByAngleCounterClockwise(b, -225)
        self.assertAlmostEqual(3 - sqrt(2), a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(3, a.y, 8, msg + " " + case + ": y coordinate is wrong")   
       
   
    def test_translateByAngleCounterClockwise_neg315(self):      
        #Check rotate by -315 degree

        msg = "Rotated by -315 degree counter-clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)

        a.translateByAngleCounterClockwise(b, -315)
        self.assertAlmostEqual(0, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(sqrt(2), a.y, 8, msg + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)

        a.translateByAngleCounterClockwise(b, -315)
        self.assertAlmostEqual(3, a.x, 8, msg + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(3 + sqrt(2), a.y, 8, msg + " " + case + ": y coordinate is wrong")       



    

if __name__ == '__main__':
    unittest.main()


