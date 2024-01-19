import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()

dictapp = {"command prompt":"cmd",
            "word":"winword",
            "excel":"excel",
            "chrome":"chrome",
            "vs code":"code"}
        
def openwebapp(query):
    if ".com" in query or ".org" in query:
        query = query.replace("search","")
        query = query.replace("open","")
        webbrowser.open(f"https://www.{query}")
    
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")
    
def closeapp(query):

    Speak("Closing, Sir")

    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        Speak("All tabs closed, Sir")

    elif "two tabs" in query or "2 tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        Speak("All tabs closed, Sir")

    elif "three tabs" in query or "3 tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        Speak("All tabs closed, Sir")

    elif "four tabs" in query or "4 tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        Speak("All tabs closed, Sir")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskKill /f /im {dictapp[app]}.exe")












                