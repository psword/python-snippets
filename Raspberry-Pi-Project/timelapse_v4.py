#import the packages we will use
from picamera import PiCamera
from time import sleep
from datetime import date
from datetime import datetime
import os


#create the new path for this photo set
recording_directory = "/home/pi/Recordings"
today = date.today()
timenow = datetime.now()
dir_date = today.strftime("%d-%b-%Y")
file_date = timenow.strftime("%d-%b-%Y_%H%M%S")
folderpath = os.path.join(recording_directory, str(dir_date))
#animationpath = os.path.join(recording_directory, str(dir_date, 'animation'))

def create_date_dir():

    if not os.path.exists(recording_directory):
        os.mkdir(recording_directory)
        
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)

create_date_dir()

#set up the camera
camera = PiCamera()
#sleep(30)

#show the camera preview
#camera.start_preview() 
#take a set amount of photos
for i in range (0, 9):
    os.chdir(folderpath)
    #camera.start_preview() #show the camera preview
    #take a picture
    #but now we need the files to be named sequentially
    #here we use the current value of i and append it to the filename
    #you could use a timestamp instead
    #camera.capture('img%s.jpg' % i)
    camera.capture('img%s.jpg' % file_date)
    sleep (0.25)

#close the preview
#camera.stop_preview()

#now we need to convert the images into a gif for the timelapse
#import the system package
#for a timelapse (GIF) we now need Image Magick
#use sudo apt-get install imagemagick -y
from os import system
system('convert -delay 1 -loop 0 img*jpg animation.gif')
os.rename('animation.gif', 'animation%s.gif' %file_date)


#since this takes a while to run, add a print statement
#print ('done creating the animation')




