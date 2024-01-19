import pywhatkit
import speech_recognition as sr
import pyttsx3
import webbrowser as wb
import requests
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
from time import sleep
import wikipedia as googleScrap
import pywhatkit
from bs4 import BeautifulSoup
import requests
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()

def TakeCommand_eng():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print(": Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f": Your Command : {query}\n")
    except:
        return ""
    return query.lower()

query = TakeCommand_eng().lower()



def myloc(query):
    Speak("Checking, Sir...")

    ip_add = requests.get("https://api.ipify.org").text
    url = "https://get.geojs.io/v1/ip/geo/" + str(ip_add) + ".json"
    wb.open(url)
    geo_q = requests.get(url)
    geo_d = geo_q.json()
    state = geo_d["city"]
    country = geo_d["country"]
    location_info = f"You are currently in {state}, {country}."
    Speak(location_info)





def GoogleSearch(query):
    if "in google" in query or "google" in query or "Google" in query:
        query = query.replace("google", "")
        query = query.replace("search", "")
        try:
            Speak("This is what you want, Sir")
            pywhatkit.search(query)

            # Fetch information from Wikipedia
            result = wikipedia.summary(query, sentences=2)
            
            if result:
                Speak(result)
            else:
                Speak("No information found on Wikipedia.")
                
        except Exception as e:
            print(e)
            Speak("Try again Sir...")


