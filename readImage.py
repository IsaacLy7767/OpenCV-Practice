import cv2 as cv

def rescaleFrame(frame, scale=0.75): # Resizing function
    width = int(frame.shape[1] * scale) # Resize width to scale
    height = int(frame.shape[0] * scale) # Resize height to scale
    dimensions = (width,height) # Create tuple with width and height

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA) # resizes frame to particular scale

img = cv.imread("TestImage.png") # Read image from file and set to variable

cv.imshow('image', img) # Display image in new window



resized_img = rescaleFrame(img) # Create resized image
cv.imshow("resized image", resized_img) # Display resized image in new window

cv.waitKey(0) # Close window when any key is pressed

