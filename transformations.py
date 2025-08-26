import cv2 as cv
import numpy as np

# .shape[#] = [height, width, number of channels]

img = cv.imread('TestImage.png')

cv.imshow('Image',img)

# Translation
# Function to translate images
def translate(img, x, y):
    # +x = right    -x = left
    # +y = down     -y = up
    transMat = np.float32([[1,0,x],[0,1,y]]) # Create translation matrix
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# Roatation
# Can rotate around any point
# Can rotate a roated image
# Black space will be included in the rotation
def rotate(img, angle, rotPoint=None):
    # +angle = counter-clockwise    -angle = clockwise
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# Flipping
flip = cv.flip(img, 0)
# flipCode = 0: flip on x-axis/vertically
# flipCode = 1: flip on y-axis/horizontally
# flipCode = -1: flip on both axes
cv.imshow('Flip', flip)

# Resize found in basic.py
# Cropping found in basic.py

cv.waitKey(0)