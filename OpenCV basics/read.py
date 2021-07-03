from rescale import rescaleFrame
import cv2 as cv

# Reading images
# img = cv.imread('Photos/cat2.jpg')

# width = 960
# height = 540
# dim = (width, height)
# resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)


# cv.namedWindow("Cat", cv.WINDOW_NORMAL)
# cv.resizeWindow("Cat", width, height)
# cv.moveWindow("Cat", 0, 0)

# cv.imshow('Cat', resized)

# cv.waitKey(0)

# Reading videos
# VideoCapture(integer) = takes video frame from camera (0 = webcam/first cam)
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, 0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
