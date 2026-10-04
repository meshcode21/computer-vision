import cv2 as cv
import mediapipe as mp
import os

# read image
image_path = os.path.join("public","faces.jpg")
image = cv.imread(image_path)

H, W, _ = image.shape

# detect faces in the image using mediapipe
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
    image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    results = face_detection.process(image_rgb)
    
    if results.detections is not None:
        for detection in results.detections:
            bbox = detection.location_data.relative_bounding_box
            x, y, w, h = int(bbox.xmin * W), int(bbox.ymin * H), int(bbox.width * W), int(bbox.height * H)
            
            # cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # draw bounding box
            # blur faces
            # face_roi = image[y:y+h, x:x+w]
            # face_roi = cv.GaussianBlur(face_roi, (31, 31), 20) # blur the face region
            # image[y:y+h, x:x+w] = face_roi

            cv.blur(image[y:y+h, x:x+w], (30, 30), dst=image[y:y+h, x:x+w])  # blur the face region

# save image in current directory
cv.imwrite("output/blurred_faces.jpg", image)


# cv.imshow("Original Image", image)
# cv.waitKey(0)