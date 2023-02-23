import cv2
import numpy as np
import os
import threading
import queue

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

    def outputColor2(color):
        os.system("afplay "+f"speech/{color}des.mp3")


def detect(cap, message_queue):
    while True:
        _, frame = cap.read()
        frame = cv2.resize(frame, (640, 640))
        color = ColorDetection.detectColor(frame)
        print(color)
        message_queue.put(frame)
        message_queue.put(color)
        key = cv2.waitKey(1)
        if key == ord('q'):
            message_queue.put('quit')
            break
        elif key == ord('p'):
            ColorDetection.outputColor2(color)
    cap.release()

def showFrame(message_queue):
    while True:
        message = message_queue.get()
        if message == 'quit':
            break
        frame = message
        color = message_queue.get()
        cv2.imshow('Frame', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            message_queue.put('quit')
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    message_queue = queue.Queue()
    t1 = threading.Thread(target=detect, args=(cap, message_queue))
    t2 = threading.Thread(target=showFrame, args=(message_queue,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
