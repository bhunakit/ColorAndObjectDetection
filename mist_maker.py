import time
import serial

color = cl

def sendcolor(color): 
    arduino = serial.Serial('/dev/cu.usbmodem11301', 115200, timeout=10) #gonna check port later
    time.sleep(1)

    while True:
        if color == 'Red' :
            arduino.write(b'Red')
        
        if color == 'Blue' :
            arduino.write(b'Blue')
        
        if color == 'Green' :
            arduino.write(b'Green')