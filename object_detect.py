from ultralytics import YOLO
import cv2
import numpy as np
import os
from color_recog import ColorDetection

model = YOLO('v6_150.pt')
cap = cv2.VideoCapture(0)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 640))

    re = model.predict(source=frame, conf=0.7)
    cv2.imshow('frame', frame)

    key = cv2.waitKey(100)  

    try:
        # detect and assign object
        obj = np.array(re[0].boxes.cls).astype(int)[0]
        objdic = {4:'phone', 1:'banknote', 3:'mask', 0:'backpack', 2:'card'}
        object = objdic[obj]

        # detect and assign color
        color = ColorDetection.detectColor(frame)

        print(f'OBJECT: {object}, COLOR: {color}')

    except:
        print("Undetected")
    
    if key == ord('q'):
        break
    elif key == ord('e'):
        ColorDetection.outputColor(object, color, 'en')
    elif key == ord('t'):
        ColorDetection.outputColor(object, color, 'th')

cap.release()
cv2.destroyAllWindows()
