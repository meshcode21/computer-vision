import cv2 as cv
import mediapipe as mp
import os

# read image
image_path = os.path.join("public","faces.jpg")
image = cv.imread(image_path)

# detect faces in the image using mediapipe
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
    image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    results = face_detection.process(image_rgb)
    
    print(results)

# blur faces

# save image

cv.imshow("Original Image", image)
cv.waitKey(0)