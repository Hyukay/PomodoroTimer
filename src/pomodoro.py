##create a pomodoro timer that reminds you to push your code every 15 minutes
    
import time
import datetime
import os
import sys
import subprocess
import pyttsx3
import speech_recognition as sr
import webbrowser
import random




#get the current time
def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")


#function that checks