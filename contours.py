import cv2 as cv
import numpy as np

# Contours - line or curve that joins continuous points long the boundry of an object
# Useful for shape analysis and object detection and recognition

img = cv.imread('TestImage.png')

cv.imshow('Image',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Can use canny or threshold

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# canny = cv.Canny(blur, 125, 175,)
# cv.imshow('Canny Edges', canny)


ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.threshold - if a pixel's intnesity does not surpase the threshold, it will be set to 0/blank, else it will be set to the maximum/third argument
# Takes grayscale image
cv.imshow('Tresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# Mode:
    # cv.RETR_TREE - for all hierarchical contours
    # cv.RETR_EXTERNAL - for all external contours
    # cv.RETR_LIST - for all contours in image
# Method:
    # cv.CHAIN_APPROX_NONE - returns all coordiate points of contours
    # cv.CHAIN_APPROX_SIMPLE - will compress all the points into ones that make sense   (eg. 2 end points of a line)
# findContours returns:
    # Contours - puthon list of all coordinate of contours in image
    # Hierarchies - hierarchical representation on contours

print(len(contours)) # Will print # of contours in image
# If too many contours, blur image

blank = np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank, contours, -1, (0,0,255), 1)
# contourIdx - # of contours that will be drawn, -1 = all
cv.imshow('Conturs', blank)


cv.waitKey(0)