#import the packages we will use
from picamera import PiCamera
from time import sleep

#set up the camera
camera = PiCamera()

#show the camera preview
#camera.start_preview()
#take a picture
camera.capture('img.jpg')
#sleep sort of pauses the code for a period of time
#gives time for us to see the window and the pi time to save the img
#sleep (3)
#close the preview
#camera.stop_preview()