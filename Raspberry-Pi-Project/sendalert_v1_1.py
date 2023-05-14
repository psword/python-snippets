#This script will send and alert to Telegram
#This uploads a file to filestack then forwards to the messenger

#Import our libraries
from picamera import PiCamera
from time import sleep
from datetime import date
from datetime import datetime
import os
import requests
from filestack import Client

client = Client("XXXXXXXXXX")
recording_directory = "/home/pi/Recordings"
today = date.today()
timenow = datetime.now()
dir_date = today.strftime("%d-%b-%Y")
#The file_date is ready if we need to use it
#file_date = timenow.strftime("_%d-%b-%Y_%H%M%S")
folderpath = os.path.join(recording_directory, str(dir_date))

def send_alert():
    #change the working directory to recordings
    os.chdir(folderpath)
    ifttt = "https://maker.ifttt.com/trigger/trigger/with/key/XXXXXXXXXX"
    new_filelink = client.upload(filepath="animation.gif")
    filestack = new_filelink.url
    print(filestack)
    
    r = requests.post(ifttt, json = {"value1" : filestack})
    if r.status_code == 200:
        print("Alert Sent")
    else:
        print("Error")

send_alert()