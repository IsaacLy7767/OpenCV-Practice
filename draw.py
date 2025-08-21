import cv2 as cv
import numpy as np

# .shape[#] = [height, width, number of channels]

blank = np.zeros((500,500,3), dtype='uint8') # Creates blank image
# 500,500 = size        (height, width)
# 3 = number of color channels/BGR
# 'uint8' = image data type

cv.imshow('Blank', blank) # Display image in new window


blank[:] = 0,255,0 # Change entire screen color
cv.imshow('Green', blank)


blank[100:200, 100:200] = 0,0,255 # Change the region to a different color      (height1:height2, width1,width2)
cv.imshow('Partial', blank)


# thickness=cv.FILLED or thickness=-1 creates filled shape
# Can use .shape to get relative points to image size

cv.rectangle(blank, (250,250), (500,500), (255,255,255), thickness=2) # Create outlined rectangle from two points
cv.imshow('Rectangle', blank)


cv.circle(blank, (400,400), 75, (255,0,0), thickness=-1) # Create circle frome center point and radius
cv.imshow('Circle', blank)


cv.line(blank, (0,500), (500,0), (255,0,255), thickness=2) # Creates line from two points
cv.imshow("Line", blank)

cv.putText(blank, 'Hello World', (250,100), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,0), 2) # Creates text from given text at a center point
cv.imshow("Text", blank)



cv.waitKey(0) # Close window when any key is pressed