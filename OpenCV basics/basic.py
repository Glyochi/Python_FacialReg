import cv2 as cv

img = cv.imread('Photos/Cat1.jpg')
cv.imshow('Cat', img)


# Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Cat', gray)

# Bluring images
# blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('Blurred Cat', blur)

# Edge Cascade
# can reduce the number of edges by applying a blur ontop of the image before running the Canny edge detection
# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny Edge', canny)
# cannyLessEdges = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Less Edges', cannyLessEdges)

# Dilating the image
# dilated = cv.dilate(canny, (7,7), iterations = 3)
# cv.imshow('Dilated Cat', dilated)

# Erode the image
# eroded = cv.erode(canny, (7,7), iterations = 3)
# cv.imshow('Eroded Cat', eroded)

# Resize the image
# resized = cv.resize(img, (max(img.shape[1]//2, 540) , max(img.shape[1]//2, 540) * img.shape[0] // img.shape[1]), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized Cat Cubic', resized)
# resized = cv.resize(img, (max(img.shape[1]//2, 540) , max(img.shape[1]//2, 540) * img.shape[0] // img.shape[1]), interpolation=cv.INTER_LINEAR)
# cv.imshow('Resized Cat Linear', resized)
# resized = cv.resize(img, (max(img.shape[1]//2, 540) , max(img.shape[1]//2, 540) * img.shape[0] // img.shape[1]), interpolation=cv.INTER_LINEAR_EXACT)
# cv.imshow('Resized Cat Linear Exact', resized)

# Cropping
# cropped = img[50:200, 200:400]
# cv.imshow('Cropped Cat', cropped)


while not cv.waitKey(0):
    69420

cv.destroyAllWindows()
