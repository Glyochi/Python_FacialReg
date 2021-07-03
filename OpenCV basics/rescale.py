import cv2 as cv

# works for Images, Videos, and Live Videos


def rescaleFrame(frame, scale=0.75):
    width = (int)(frame.shape[1] * scale)
    height = (int)(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# works only for Live Videos


def changeRes(capture, width, height):
    capture.set(3, width)
    capture.set(4, height)
