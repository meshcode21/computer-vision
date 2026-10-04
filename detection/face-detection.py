import cv2 as cv, mediapipe as mp

# read webcam
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    mp_face_detection = mp.solutions.face_detection

    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = face_detection.process(frame_rgb)
        
        if results.detections is not None:
            for detection in results.detections:
                bbox = detection.location_data.relative_bounding_box
                H, W, _ = frame.shape
                x, y, w, h = int(bbox.xmin * W), int(bbox.ymin * H), int(bbox.width * W), int(bbox.height * H)
                
                # rectangle faces
                # cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                # blur faces
                cv.blur(frame[y:y+h, x:x+w], (55, 55), dst=frame[y:y+h, x:x+w])  # blur the face region
                
    cv.imshow("Webcam Face Detection", frame)


    if cv.waitKey(40) & 0xFF == ord('q'):
        break

# release the webcam object and close all windows
cap.release()
cv.destroyAllWindows()

