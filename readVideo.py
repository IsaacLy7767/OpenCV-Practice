import cv2 as cv

def rescaleFrame(frame, scale=0.75): # Resizing function
    width = int(frame.shape[1] * scale) # Resize width to scale
    height = int(frame.shape[0] * scale) # Resize height to scale
    dimensions = (width,height) # Create tuple with width and height

    # .shape = [height, width, number of channels]

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA) # resizes frame to particular scale

def changeRes(width, height): # Change resolution function
    # Exclusive to live video
    vid.set(3, width) # Changes width
    vid.set(4, height) # Changes height

vid = cv.VideoCapture('TestVideo.mp4') # Read video from file and set instnace to variable

while True: 
    isTrue, frame = vid.read() # Use loop to grab video frame by frame
    
    frame_resize = rescaleFrame(frame) # Rescale frame

    cv.imshow('Video', frame) # Display frame in new window
    cv.imshow("Resized Video", frame_resize) # Display resized frame in new window 

    if cv.waitKey(20) & 0xFF==ord('d'): # Wait until d is pressed to break loop and stop video
        break

vid.release() # Release caputre device/release memory
cv.destroyAllWindows() # Close all window


# -215 Asserion Error : OpenCV tried to open a file that doesn't exist or it ran out of frames