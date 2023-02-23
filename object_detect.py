from ultralytics import YOLO
import cv2
import numpy as np
import os
from color_recog import ColorDetection
from pygame import mixer
import time
import serial
import time
from color_recog import  ColorDetection as cl 
    
time_bool = False

# load the model
model = YOLO('v6_150.pt')

# start up webcam
cap = cv2.VideoCapture(0)

# start sound mixer
mixer.init()

while True:
    _, frame = cap.read()
    processed = cv2.resize(frame, (640, 640))

    re = model.predict(source=processed, conf=0.6)

    try:
        # detect and assign object
        obj = np.array(re[0].boxes.cls).astype(int)[0]
        objdic = {4:'phone', 1:'banknote', 3:'mask', 0:'backpack', 2:'card'}
        object = objdic[obj]

        # detect and assign color
        color = ColorDetection.detectColor(processed)

        print(f'OBJECT: {object}, COLOR: {color}')

    except:
        print("Undetected")

    # show frame
    cv2.imshow('frame', frame)
    key = cv2.waitKey(100)  

    if key == ord('q'):
        break

    if len(re[0].boxes.cls) != 0:
        if time_bool is False:
            a = time.time()
            time_bool = True
        if time.time() - a >= 5:
            ColorDetection.outputColor(object, color, 'en')
            if color == 'red':
                #mixer.init()
                mixer.music.load('/Users/bhun/School/Robotics_Project/Push/speech/reddes.mp3')
                mixer.music.play()
            elif color == 'blue':
                #mixer.init()
                mixer.music.load('/Users/bhun/School/Robotics_Project/Push/speech/bluedes.mp3')
                mixer.music.play()
            elif color == 'green':
                #mixer.init()
                mixer.music.load('/Users/bhun/School/Robotics_Project/Push/speech/greendes.mp3')
                mixer.music.play()
            print('...................PLAYING...................')
            a= 1000000000000
    else:
        time_bool = False
        a = 0


cap.release()
cv2.destroyAllWindows()
