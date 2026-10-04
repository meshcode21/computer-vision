import cv2 as cv
from util import get_limits

# capture video from webcam

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret: 
        break

    # convert the frame to HSV color space
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    #get the lower and upper limits for the color pink
    lower_limit, upper_limit = get_limits(color = [206, 0, 246]) # pink color in BGR

    # create a mask
    mask = cv.inRange(hsv_frame, lower_limit, upper_limit)

    # find contours in the mask
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # draw rectangles around the detected contours
    for contour in contours:
        
        # eliminate small contours to reduce noise
        if cv.contourArea(contour) > 500:
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # display the resulting frame
    cv.imshow('frame', frame)
    # cv.imshow('mask', mask)

    # press 'q' to exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()