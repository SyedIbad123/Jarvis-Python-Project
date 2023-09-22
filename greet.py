from clubui import Ui_SECRET
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def Greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        Speak("Good morning, Sir. I am Vision, your Virtual assisstant")

    elif hour >= 12 and hour <= 16:
        Speak("Good afternoon , sir.  I am Vision, your Virtual assisstant")
    else:
        Speak("Good evening, sir.  I am Vision, your Virtual assisstant")

