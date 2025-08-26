import cv2 as cv

img = cv.imread('TestImage.png')

cv.imshow('Image',img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
# ksize = kernal size 
#   must be an odd number
#   increasing number increases intensity of blur
cv.imshow('Blur', blur)

# Edge Cascade - find the edges present in an image
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# Dialating image - dialate specific structuring element    (eg. canny edges)
dilated = cv.dilate(canny, (3,3), 1)
# Increasing kernal size and iterations increases thickness
cv.imshow('Dialted', dilated)

# Eroding - similar to undoing dialation, not perfect
eroded = cv.erode(dilated, (3,3), 1)
cv.imshow('Eroded', eroded)

# Resize
resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
# Will resize image to given dimensions, ignoring aspect ratios
# Interpoations
#   INTER_AREA - good when shrinking image
#   INTER_LINEAR - good when enlarging image
#   INTER_CUBIC - good when enlarging image, slower but higher quality
cv.imshow('Resize', resize)

# Cropping
cropped = img[150:300, 400:600]
# img is an array, using array cropping to crop image
# [x:x, y:y]
cv.imshow('Cropped', cropped)

cv.waitKey(0)