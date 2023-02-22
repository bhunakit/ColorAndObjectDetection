import cv2
import numpy as np
import os

class ColorDetection:
    def __init__(self, cap):
        self.cap = cap

    def detectColor(frame):
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Red Color
        low_red = np.array([161, 155, 84])
        high_red = np.array([179, 255, 255])
        red_mask = cv2.inRange(hsv_frame, low_red, high_red)
        red = cv2.bitwise_and(frame, frame, mask=red_mask)

        red_amount = np.sum(red)

        # Blue color
        low_blue = np.array([94, 80, 2])
        high_blue = np.array([126, 255, 255])
        blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
        blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

        blue_amount = np.sum(blue)

        # Green color
        low_green = np.array([25, 52, 72])
        high_green = np.array([102, 255, 255])
        green_mask = cv2.inRange(hsv_frame, low_green, high_green)
        green = cv2.bitwise_and(frame, frame, mask=green_mask)

        green_amount = np.sum(green)

        max = np.max([red_amount, green_amount, blue_amount])
        if max == red_amount:
            # cv2.imshow('segment', red)
            return "red"
        elif max == green_amount:
            # cv2.imshow('segment', green)
            return "green"
        elif max == blue_amount:
            # cv2.imshow('segment', blue)
            return "blue"
        else:
            pass
    
    def outputColor(object, color, lang):
        if lang == 'en':
            os.system("afplay "+ f"speech/{color}.mp3")
            os.system("afplay "+ f"speech/{object}.mp3")
        elif lang == 'th':
            colordic = {'red': 'สีแดง', 'blue': 'สีน้ำเงิน', 'green': 'สีเขียว'}
            objdic = {'backpack': 'เป้', 'card': 'การ์ด', 'mask': 'หน้ากาก', 'phone': 'โทรศัพท์', 'banknote': 'ธนบัตร'}
            os.system("afplay "+ f"speech/{objdic[object]}.mp3")
            os.system("afplay "+ f"speech/{colordic[color]}.mp3")
        else:
            pass

# cap = cv2.VideoCapture(0)

# while True:
#     _, frame = cap.read()
#     frame = cv2.resize(frame, (640,640))
#     color = ColorDetection.detectColor(frame)
#     object = 'banknote'
#     print(color)
#     cv2.imshow('g', frame)
#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break
#     elif key == ord('e'):
#         ColorDetection.outputColor(object, color, 'en')
#     elif key == ord('t'):
#         ColorDetection.outputColor(object, color, 'th')
    

# cap.release()
# cv2.destroyAllWindows()
