import cv2 as cv
from Point import Point
from DetectedArea import DetectedArea
from helperFunctions import *
import numpy as np


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
            :param img: the image/frame that we will run facial detection on
        """
        # Blank canvas that we are going to use to store the rotated image
        self.image = img
        self.grayImage = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        self.imageCenter = Point(img.shape[0]/2, img.shape[1]/2)
    

    def runHaarDetection(self, detector, scaleFactor, minNeighbors):
        """
        Call the runHaarDetectionAngle function with 0, 90, 180, and 270 degree as angle inputs to generate a 4-tuple that
        contains 4 arrays of translated DectectedArea objects with corresponding angles.
            :param detector: the haarcascade object that is going to scan the image
            :param scaleFactor: scaleFactor parameter for detectMultiScale function
            :param minNeighbors: minNeighbors parameter for detectMultiScale function
            :return a 4-tuple of 4 arrays containing all the translated coordinates of the detected objects in the image.
        """
        AllObjects = []        

        # finding objects in 90, 180, and 270 degree rotated image
        for angle in [0, 90, 180, 270]:
            
            (detected, rotatedCenter) = self.runHaarDetectionAngle(detector, angle)
            self.translateCoordinatesToOG(rotatedCenter, detected, angle, scaleFactor, minNeighbors)
            AllObjects.append(detected)

        return AllObjects    


    
    def runHaarDetectionAngle(self, detector, angle, scaleFactor, minNeighbors):
        """
        Run the given haarDetection on the image rotated by the given degree and generate 1 array that contain detected objects 
        with corresponding angle. These detected objects will be translated to have correct coordinates in the non-rotated image.
            :param detector: the haarcascade object that is going to scan the image
            :param angle: the angle by which the image is rotated
            :param scaleFactor: scaleFactor parameter for detectMultiScale function
            :param minNeighbors: minNeighbors parameter for detectMultiScale function
            :return a 2-tuple with the first element being an array containing all the relative coordinates of the detected objects in the rotated image,
            and the second element the Point object containing the coordinates of the center of the rotated image.
        """

        angle = angle % 360

        # finding objects in then given angle degree rotated image
       
        rotatedGrayImage = rotateCounterClockwise(self.grayImage, angle)
            
        # Collecting raw detected objects received from detectMultiScale
        rawObjs = detector.detectMultiScale(rotatedGrayImage, scaleFactor = scaleFactor, minNeighbors = minNeighbors)
            
        translatedObjs = []
        rotatedCenter = Point(rotatedGrayImage.shape[1]/2, rotatedGrayImage.shape[0]/2)

        for obj in rawObjs:
            # Convert raw information into DetectedArea obj
            area = DetectedArea((obj[0], obj[1]), (obj[2], obj[3]))

            # Put the translated DetectedArea into translatedObj array
            translatedObjs.append(area)

        return (translatedObjs, rotatedCenter)    


    def translateCoordinatesToOG(self, rotatedCenter, rawPositions, angle):
        """
        Translate the raw positions of the detectedAreas created using returned value of
        haarCascadeObj.detectMultiScale to the position on the original image.
            :param rawPositions: the array that contains detectedAreas with raw values taken from detectMultiScale
            :param angle: the angle by which the image was rotated when detectMultiScale ran
            :return an array containing detectedAreas with translated coordinates in the non-rotated image
        """
        angle = angle % 360
        if angle == 0:
            return rawPositions

        # Translate the coordinates to the coordinates in the non-rotated image
        for area in rawPositions:
            area.rotateAreaClockwise(self.imageCenter, angle)
            area.projectRectangle(rotatedCenter, self.imageCenter)

        return rawPositions


        

    def mergeDetectedObjs(self, four_tuple):
        """
        Given a four-tuple containing 4 arrays of detected objects, scan through all of them and if find two duplicates (similar detected objects with similar 
        sizes and positions), merge them and put all the unique detected object in an array. 
            :return an array that contains all the unique detected objects.
        """
        (array0, array90, array180, array270) = four_tuple
        
        ###########################################################################################
        # NO TESTING DONE # NO TESTING DONE # NO TESTING DONE # NO TESTING DONE # NO TESTING DONE #
        ###########################################################################################

        for i in range(len(array0) - 1):
            for j in range(i + 1, len(array0)):
                if array0[i].similarSize(array0[j]) and array0[i].overlap(array0[j]):
                        array0[i].merge(array0[j])
                        array0.pop(j)
                        j = j - 1

        for array in (array90, array180, array270):
            for area in array:
                matched = False
                # Scan through the array to find matches
                for area0 in array0:
                    if area0.similarSize(area) and area0.overlap(area):
                        area0.merge(area)
                        matched = True
                        break
                
                # if didnt find any matches then append it onto array0
                if matched == False:
                    array0.append(area)    
        
        return array0





    def findEyes(self):
        """
        Find the eyes in the image after applying haarcascade eye detection on the 0, 90, 180, and 270 degree rotated image. 
        Collect all the detected eyes and remove duplicates. 
            :return an array of detected eyes
        """
        return self.mergeDetectedObjs(self.runHaarDetection(self.haarcascade_eye)


)