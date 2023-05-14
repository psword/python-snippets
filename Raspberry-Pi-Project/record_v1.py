#This script will record a video
#For testing purposes, we will initially consider 60 seconds

from picamera import PiCamera
from time import sleep
from subprocess import call
from datetime import date
from datetime import datetime
import os

#initialize the camera
camera = PiCamera()
camera.framerate = 15

def take_video(file_h264, file_mp4):
    #Record for 60 seconds
    camera.start_recording(file_h264)
    sleep(60)
    camera.stop_recording()
    #Convert from H264 to MP4
    command = "MP4Box -add " + file_h264 + " " + file_mp4
    call([command], shell=True)

#change the working directory to recordings
recording_directory = "/home/pi/Recordings"
today = date.today()
timenow = datetime.now()
dir_date = today.strftime("%d-%b-%Y")
#The file_date is ready if we need to use it
file_date = timenow.strftime("_%d-%b-%Y_%H%M%S")
folderpath = os.path.join(recording_directory, str(dir_date))
os.chdir(folderpath)

#Invoke the function
take_video('test.h264', 'test.mp4')
#here is a rename option if we need it
os.rename('test.mp4', 'video-record%s.mp4' %file_date)
os.remove('test.h264')