#import the packages we will use
from picamera import PiCamera
from time import sleep

#for a timelapse (GIF) we now need Image Magick
#use sudo apt-get install imagemagick -y

#import the new package
from os import system

#set up the camera
camera = PiCamera()
#sleep(30)

#take a set amount of photos
for i in range (0, 9):
    #camera.start_preview() #show the camera preview
    #take a picture
    #but now we need the files to be named sequentially
    #here we use the current value of i and append it to the filename
    #you could use a timestamp instead
    camera.capture('img%s.jpg' % i) 
    sleep (0.25)
    #camera.stop_preview() #close the preview

#now we need to convert the images into a gif for the timelapse
system('convert -delay 1 -loop 0 img*jpg animation.gif')

#since this takes a while to run, add a print statement
#print ('done creating the animation')

