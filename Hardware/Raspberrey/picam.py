import cv2
import time
from picamera2 import Picamera2

picam = Picamera2()
picam.preview_configuration.main.size=(1280,720)
picam.preview_configuration.main.format="RGB888"
picam.preview_configuration.align()
picam.configure("preview")
picam.start()
print("picamera2 is on")






print(cv2.__version__)
#dispW=1280
#dispH=720
#cam=cv2.VideoCapture('/videos/vid0')
#cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

while True:
    im= picam.capture_array()
    cv2.imshow('Camera',im)
    if cv2.waitKey(1)==ord('q'):
        break
#cam.release()
cv2.destroyAllWindows()






