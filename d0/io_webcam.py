import os
import cv2

# read webcam
webcam = cv2.VideoCapture(0)
 
# visualize webcam
while True:
    ret, frame = webcam.read()
    if not ret:
        break
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

# release the webcam object and close all windows
webcam.release()
cv2.destroyAllWindows()