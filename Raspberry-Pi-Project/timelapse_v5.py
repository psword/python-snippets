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
#The file_date is ready if we need to use it
#file_date = timenow.strftime("_%d-%b-%Y_%H%M%S")
folderpath = os.path.join(recording_directory, str(dir_date))

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
camera.start_preview() 
#take a set amount of photos

#change the working directory to recordings
os.chdir(folderpath)

for i in range (0, 9):
    
    #camera.start_preview() #show the camera preview
    #take a picture
    #but now we need the files to be named sequentially
    #here we use the current value of i and append it to the filename
    #you could use a timestamp instead
    camera.capture('img%s.jpg' % i)
    sleep (0.25)

#close the preview
camera.stop_preview()







