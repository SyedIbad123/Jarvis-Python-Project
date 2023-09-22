import pywhatkit
import speech_recognition as sr
import pyttsx3
import webbrowser as wb
import requests
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
from time import sleep
from googletrans import Translator
from gtts import gTTS
import googletrans
import os
import playsound
import time

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

def GoogleSearch(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("vision","")
        query = query.replace("google","")
        query = query.replace("search","")
        try:
            Speak("This is what you want, Sir")
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            Speak(result)     
        except Exception as e:
            print(e)
            Speak("Try again Sir...")

def SearchYoutube(query):
    if "YouTube" in query:
        Speak("This is what i found for your search!")
        query = query.replace("youtube search","")
        query = query.replace("search","")
        query = query.replace("youtube","")
        query = query.replace("vision","")
        web = "https://www.youtube.com/results?search_query=" + query
        wb.open(web)
        pywhatkit.playonyt(query)
        Speak("Done, Sir")

def myloc(query):
    op = "https://www.google.com/maps/place/Karachi,+Karachi+City,+Sindh,+Pakistan/@25.1933894,66.594933,9z/data=!3m1!4b1!4m5!3m4!1s0x3eb33e06651d4bbf:0x9cf92f44555a0c23!8m2!3d24.8607343!4d67.0011364"
    Speak("checking, Sir...")
    wb.open(op)
    ip_add = requests.get("https://api.ipify.org").text
    url = "https://get.geojs.io/v1/ip/geo/" + str(ip_add) + ".json"
    geo_q = requests.get(url)
    geo_d = geo_q.json()
    state = geo_d["city"]
    country = geo_d["country"]
    Speak(f"Sir, You are currently in {state, country} ")

def googleMap(place):
    try:
        url_place = "https://www.google.com/maps/place/" + str(place)
        geo_locator = Nominatim(user_agent="myGeocoder")
        location = geo_locator.geocode(place,addressdetails=True)
        target_latlon = location.latitude , location.longitude
        wb.open(url=url_place)
        location = location.raw['address']
        target = {"city" : location.get("city","")}
        current_loc = geocoder.ip("me")
        current_latlon = current_loc.latlng
        distance = str(great_circle(current_latlon,target_latlon))
        distance = str(distance.split(" ",1)[0])
        distance = round(float(distance),2)
        # Speak(target)
        Speak(f"sir, {place} is {distance} kilometres away from your location")
    except Exception as e:
        print(e)
        Speak("Try again, Sir")
    
def Translate(query):
    Speak("sure Sir")
    print(googletrans.LANGUAGES)
    translator = Translator()
    Speak("choose the language in which you want to translate")
    b = input("To lang :")
    text_to_translate = translator.translate(query,src = "auto",dest = b)
    text = text_to_translate.text
    try:
        query = query.replace("vision","")
        query = query.replace("translate","")
        speakg1 = gTTS(text=text,lang=b,slow=False)
        speakg1.save("voice.mp3")
        playsound("voice.mp3")

        time.sleep(5)
        os.remove("voice.mp3")
    except:
        print("unable to translate")

