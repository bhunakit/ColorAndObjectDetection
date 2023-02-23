from ultralytics import YOLO
import cv2

model = YOLO('v6_150.pt')

# start up webcam
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 640))

    re = model.predict(source=frame, conf=0.7)

    print(re[0].boxes.boxes)

    cv2.imshow('frame', frame)
    key = cv2.waitKey(100)  

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()