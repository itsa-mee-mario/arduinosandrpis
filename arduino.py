

from pyfirmata import SERVO
from pyfirmata import Arduino, util
import threading
import time
import pyfirmata
import cv2
#
print('loading')
board = pyfirmata.Arduino('/dev/ttyACM0')
print('connected to board')


def find_faces(video_device):
   cascade_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
   camera = cv2.VideoCapture(video_device)
   while True:
       frame_read, frame = camera.read()
       face_id = cascade_classifier.detectMultiScale(frame, 1.3, 5)
       for (x, y, w, h) in face_id:
           bb = cv2.rectangle(frame, (x, y), (x+w, y+h), (200, 200, 200))
           cv2.imshow("faces", bb)
       
       if cv2.waitKey(1) == ord("q"):
           break
   camera.release()
   cv2.destroyAllWindows()


#def move_cam(direction):
#    pass

#find_faces(0)


def check_relays():
        pin = []
        for i in range(2, 14):
            pin.append(board.get_pin("d:"+str(i)+":o"))
            while True:
                for i in pin:    
                    i.write(1)
            

check_relays()
