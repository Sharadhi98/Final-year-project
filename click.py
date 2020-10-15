from picamera import PiCamera
from PIL import Image
from time import sleep

def takePicture():
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture('./images/funny.png')    
    camera.stop_preview()