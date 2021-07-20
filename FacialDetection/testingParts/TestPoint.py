import unittest
from math import sqrt

import sys
sys.path.append('FacialDetection')
from Point import Point

class TestPointMethods(unittest.TestCase):



    def test_distTo(self):
        for x in range (-10, 10):
            for y in range (-10, 10):
                for j in range (-10, 10):
                    for k in range (-10, 10):
                        a = Point(x, y)
                        b = Point(j, k)
                        distance = sqrt((x - j)**2 + (y - k)**2)
                        self.assertEqual(distance, a.distTo(b), "distTo function is dead")

    
    def test_projectPoint(self):
        
        a = Point(5, 5)
        b = Point(1, 2)
        c = Point( 16, 2)
        d = a.projectPoint(b, c)
        self.assertEqual(20, d.x, "projectPoint x is wrong")
        self.assertEqual(5, d.y, "projectPoint y is wrong")
                
    def test_rotateByAngle_90(self):        
        #Check rotate by 90 degree
        
        msg1 = "Rotated by 90 degree counter-clockwise"
        msg2 = "Rotated by 90 degree clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a = a.rotatePointCounterClockwise(b, 90)
        self.assertAlmostEqual(1, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(-1, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")
        
        a = a.rotatePointClockwise(b, 90)
        self.assertAlmostEqual(1, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a = a.rotatePointCounterClockwise(b, 90)
        self.assertAlmostEqual(4, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(2, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")

        a = a.rotatePointClockwise(b, 90)
        self.assertAlmostEqual(4, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")


    def test_rotateByAngle_180(self):  
        #Check rotate by 180 degree
        
        msg1 = "Rotated by 180 degree counter-clockwise"
        msg2 = "Rotated by 180 degree clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a = a.rotatePointCounterClockwise(b, 180)
        self.assertAlmostEqual(-1, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(-1, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")

        a = a.rotatePointClockwise(b, 180)
        self.assertAlmostEqual(1, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a = a.rotatePointCounterClockwise(b, 180)
        self.assertAlmostEqual(2, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(2, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")
        
        a = a.rotatePointClockwise(b, 180)
        self.assertAlmostEqual(4, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

 
    def test_rotateByAngle_270(self):        
        #Check rotate by 270 degree
        
        msg1 = "Rotated by 270 degree counter-clockwise"
        msg2 = "Rotated by 270 degree clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a = a.rotatePointCounterClockwise(b, 270)
        self.assertAlmostEqual(-1, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")
        
        a = a.rotatePointClockwise(b, 270)
        self.assertAlmostEqual(1, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a = a.rotatePointCounterClockwise(b, 270)
        self.assertAlmostEqual(2, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg1 + " " + case + ": y coordinate is wrong") 
        
        a = a.rotatePointClockwise(b, 270)
        self.assertAlmostEqual(4, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")   
       
   
    def test_rotateByAngle_360(self):      
        #Check rotate by 360 degree

        msg1 = "Rotated by 360 degree counter-clockwise"
        msg2 = "Rotated by 360 degree clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)

        a = a.rotatePointCounterClockwise(b, 360)
        self.assertAlmostEqual(1, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")

        a = a.rotatePointClockwise(b, 360)
        self.assertAlmostEqual(1, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)

        a = a.rotatePointCounterClockwise(b, 360)
        self.assertAlmostEqual(4, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")    

        a = a.rotatePointClockwise(b, 360)
        self.assertAlmostEqual(4, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")       


#########################################################################################################################
#########################################################################################################################


    def test_rotateByAngle_45(self):        
        #Check rotate by 45 degree
        
        msg1 = "Rotated by 45 degree counter-clockwise"
        msg2 = "Rotated by 45 degree clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a = a.rotatePointCounterClockwise(b, 45)
        self.assertAlmostEqual(sqrt(2), a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(0, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")
        
        a = a.rotatePointClockwise(b, 45)
        self.assertAlmostEqual(1, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a = a.rotatePointCounterClockwise(b, 45)
        self.assertAlmostEqual(3 + sqrt(2), a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(3, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")
        
        a = a.rotatePointClockwise(b, 45)
        self.assertAlmostEqual(4, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")


    def test_rotateByAngle_135(self):  
        #Check rotate by 135 degree
        
        msg1 = "Rotated by 135 degree counter-clockwise"
        msg2 = "Rotated by 135 degree clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a = a.rotatePointCounterClockwise(b, 135)
        self.assertAlmostEqual(0, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(-sqrt(2), a.y, 8, msg1 + " " + case + ": y coordinate is wrong")
        
        a = a.rotatePointClockwise(b, 135)
        self.assertAlmostEqual(1, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a = a.rotatePointCounterClockwise(b, 135)
        self.assertAlmostEqual(3, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(3 - sqrt(2), a.y, 8, msg1 + " " + case + ": y coordinate is wrong")
        
        a = a.rotatePointClockwise(b, 135)
        self.assertAlmostEqual(4, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

 
    def test_rotateByAngle_225(self):        
        #Check rotate by 225 degree
        
        msg1 = "Rotated by 225 degree counter-clockwise"
        msg2 = "Rotated by 225 degree clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a = a.rotatePointCounterClockwise(b, 225)
        self.assertAlmostEqual(-sqrt(2), a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(0, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")
        
        a = a.rotatePointClockwise(b, 225)
        self.assertAlmostEqual(1, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a = a.rotatePointCounterClockwise(b, 225)
        self.assertAlmostEqual(3 - sqrt(2), a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(3, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")
        
        a = a.rotatePointClockwise(b, 225)
        self.assertAlmostEqual(4, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")   
       
   
    def test_rotateByAngle_315(self):      
        #Check rotate by 315 degree

        msg1 = "Rotated by 315 degree counter-clockwise"
        msg2 = "Rotated by 315 degree clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)

        a = a.rotatePointCounterClockwise(b, 315)
        self.assertAlmostEqual(0, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(sqrt(2), a.y, 8, msg1 + " " + case + ": y coordinate is wrong")

        a = a.rotatePointClockwise(b, 315)
        self.assertAlmostEqual(1, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)

        a = a.rotatePointCounterClockwise(b, 315)
        self.assertAlmostEqual(3, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(3 + sqrt(2), a.y, 8, msg1 + " " + case + ": y coordinate is wrong")    

        a = a.rotatePointClockwise(b, 315)
        self.assertAlmostEqual(4, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")       



#########################################################################################################################
#########################################################################################################################

        
    def test_rotateByAngle_neg90(self):        
        #Check rotate by -90 degree
        
        msg1 = "Rotated by -90 degree counter-clockwise"
        msg2 = "Rotated by -90 degree clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a = a.rotatePointCounterClockwise(b, -90)
        self.assertAlmostEqual(-1, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")
        
        a = a.rotatePointClockwise(b, -90)
        self.assertAlmostEqual(1, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a = a.rotatePointCounterClockwise(b, -90)
        self.assertAlmostEqual(2, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")
        
        a = a.rotatePointClockwise(b, -90)
        self.assertAlmostEqual(4, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")


    def test_rotateByAngle_neg180(self):  
        #Check rotate by -180 degree
        
        msg1 = "Rotated by -180 degree counter-clockwise"
        msg2 = "Rotated by -180 degree clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a = a.rotatePointCounterClockwise(b, -180)
        self.assertAlmostEqual(-1, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(-1, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")
        
        a = a.rotatePointClockwise(b, -180)
        self.assertAlmostEqual(1, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a = a.rotatePointCounterClockwise(b, -180)
        self.assertAlmostEqual(2, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(2, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")
        
        a = a.rotatePointClockwise(b, -180)
        self.assertAlmostEqual(4, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

 
    def test_rotateByAngle_neg270(self):        
        #Check rotate by -270 degree
        
        msg1 = "Rotated by -270 degree counter-clockwise"
        msg2 = "Rotated by -270 degree clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a = a.rotatePointCounterClockwise(b, -270)
        self.assertAlmostEqual(1, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(-1, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")
        
        a = a.rotatePointClockwise(b, -270)
        self.assertAlmostEqual(1, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a = a.rotatePointCounterClockwise(b, -270)
        self.assertAlmostEqual(4, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(2, a.y, 8, msg1 + " " + case + ": y coordinate is wrong") 
        
        a = a.rotatePointClockwise(b, -270)
        self.assertAlmostEqual(4, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")   
       
   
    def test_rotateByAngle_neg360(self):      
        #Check rotate by -360 degree

        msg1 = "Rotated by -360 degree counter-clockwise"
        msg2 = "Rotated by -360 degree clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)

        a = a.rotatePointCounterClockwise(b, -360)
        self.assertAlmostEqual(1, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")

        a = a.rotatePointClockwise(b, -360)
        self.assertAlmostEqual(1, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)

        a = a.rotatePointCounterClockwise(b, -360)
        self.assertAlmostEqual(4, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")     

        a = a.rotatePointClockwise(b, -360)
        self.assertAlmostEqual(4, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")       


#########################################################################################################################
#########################################################################################################################


    def test_rotateByAngle_neg45(self):        
        #Check rotate by -45 degree
        
        msg1 = "Rotated by -45 degree counter-clockwise"
        msg2 = "Rotated by -45 degree clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a = a.rotatePointCounterClockwise(b, -45)
        self.assertAlmostEqual(0, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(sqrt(2), a.y, 8, msg1 + " " + case + ": y coordinate is wrong")
        
        a = a.rotatePointClockwise(b, -45)
        self.assertAlmostEqual(1, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a = a.rotatePointCounterClockwise(b, -45)
        self.assertAlmostEqual(3, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(3 + sqrt(2), a.y, 8, msg1 + " " + case + ": y coordinate is wrong")
        
        a = a.rotatePointClockwise(b, -45)
        self.assertAlmostEqual(4, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")


    def test_rotateByAngle_neg135(self):  
        #Check rotate by -135 degree
        
        msg1 = "Rotated by -135 degree counter-clockwise"
        msg2 = "Rotated by -135 degree clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a = a.rotatePointCounterClockwise(b, -135)
        self.assertAlmostEqual(-sqrt(2), a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(0, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")
        
        a = a.rotatePointClockwise(b, -135)
        self.assertAlmostEqual(1, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a = a.rotatePointCounterClockwise(b, -135)
        self.assertAlmostEqual(3 - sqrt(2), a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(3, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")
        
        a = a.rotatePointClockwise(b, -135)
        self.assertAlmostEqual(4, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

 
    def test_rotateByAngle_neg225(self):        
        #Check rotate by -225 degree
        
        msg1 = "Rotated by -225  degree counter-clockwise"
        msg2 = "Rotated by -225 degree clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)
        
        a = a.rotatePointCounterClockwise(b, -225)
        self.assertAlmostEqual(0, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(-sqrt(2), a.y, 8, msg1 + " " + case + ": y coordinate is wrong")
        
        a = a.rotatePointClockwise(b, -225)
        self.assertAlmostEqual(1, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)
        
        a = a.rotatePointCounterClockwise(b, -225)
        self.assertAlmostEqual(3, a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(3 - sqrt(2), a.y, 8, msg1 + " " + case + ": y coordinate is wrong")  
        
        a = a.rotatePointClockwise(b, -225)
        self.assertAlmostEqual(4, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")   
       
   
    def test_rotateByAngle_neg315(self):      
        #Check rotate by -315 degree

        msg1 = "Rotated by -315 degree counter-clockwise"
        msg2 = "Rotated by -315 degree clockwise"

        #Case 1
        case = "CASE 1"
        a = Point(1,1)
        b = Point(0,0)

        a = a.rotatePointCounterClockwise(b, -315)
        self.assertAlmostEqual(sqrt(2), a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(0, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")

        a = a.rotatePointClockwise(b, -315)
        self.assertAlmostEqual(1, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(1, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")

        #Case 2
        case = "CASE 2"
        a = Point(4, 4)
        b = Point(3, 3)

        a = a.rotatePointCounterClockwise(b, -315)
        self.assertAlmostEqual(3 + sqrt(2), a.x, 8, msg1 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(3, a.y, 8, msg1 + " " + case + ": y coordinate is wrong")     

        a = a.rotatePointClockwise(b, -315)
        self.assertAlmostEqual(4, a.x, 8, msg2 + " " + case + ": x coordinate is wrong")
        self.assertAlmostEqual(4, a.y, 8, msg2 + " " + case + ": y coordinate is wrong")       



    

if __name__ == '__main__':
    unittest.main()


