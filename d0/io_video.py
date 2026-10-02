import cv2
import os

# read video
video_path = os.path.join('public', 'earth.mp4')
video = cv2.VideoCapture(video_path)

# visualize video
while True:
    ret, frame = video.read()
    if not ret:
        break
    cv2.imshow("Video", frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

# release the video capture object and close all windows
video.release()
cv2.destroyAllWindows()