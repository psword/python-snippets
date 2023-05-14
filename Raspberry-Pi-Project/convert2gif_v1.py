#now we need to convert the images into a gif for the timelapse
#import the system package
#for a timelapse (GIF) we now need Image Magick
#use sudo apt-get install imagemagick -y
from os import system
from os import rename
import os
from datetime import date
from datetime import datetime

#change the working directory to recordings
recording_directory = "/home/pi/Recordings"
today = date.today()
timenow = datetime.now()
dir_date = today.strftime("%d-%b-%Y")
#The file_date is ready if we need to use it
#file_date = timenow.strftime("_%d-%b-%Y_%H%M%S")
folderpath = os.path.join(recording_directory, str(dir_date))
os.chdir(folderpath)

system('convert -delay 1 -loop 0 img*jpg animation.gif')
#here is a rename option if we need it
#rename('animation.gif', 'animation%s.gif' %file_date)


#since this takes a while to run, add a print statement
#print ('done creating the animation')