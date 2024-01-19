import json 
import keyboard
import re
from bardapi import BardCookies 
import datetime
import pyperclip 
import pyautogui 
import webbrowser
import speech_recognition as sr
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



user_input = None

def CookieScrapper():
    print("")
    print("*The extraction of essential cookies from GoogleBard has been accomplished successfully.*")
    webbrowser.open("https://bard.google.com")
    sleep(6)
    pyautogui.click(x=1158, y=104)
    sleep(4)
    pyautogui.click(x=869, y=145)
    sleep(2)
    keyboard.press_and_release('ctrl + w')
    sleep(2)

    data = pyperclip.paste()

    try:
        json_data = json.loads(data)
        Speak("*The process of loading cookies has been executed without any issues, and the cookies are now successfully integrated into the system.*")
        pass

    except json.JSONDecodeError as e:
        Speak("*Cookies Loaded Unsuccessfully*")
        print("""*The error has been identified as a result of unsuccessful cookie replication from the Chrome extension, 
which is causing a disruption in the intended functionality.*""")
        CookieScrapper()
     
    SID = "__Secure-1PSID"
    TS = "__Secure-1PSIDTS"
    CC = "__Secure-1PSIDCC"

    try:
        SIDValue = next((item for item in json_data if item["name"] == SID), None)
        TSValue = next((item for item in json_data if item["name"] == TS), None)
        CCValue = next((item for item in json_data if item["name"] == CC), None)

        if SIDValue is not None:
            SIDValue = SIDValue["value"]
        else:
            print(f"{SIDValue} not found in the JSON data.")

        if TSValue is not None:
            TSValue = TSValue["value"]
        else:
            print(f"{TSValue} not found in the JSON data.")
 
        if CCValue is not None:
            CCValue = CCValue["value"]
        else:
            print(f"{CCValue} not found in the JSON data.")

        cookie_dict = {
            "__Secure-1PSID": SIDValue ,
            "__Secure-1PSIDTS": TSValue,
            "__Secure-1PSIDCC": CCValue,
        }

        print("")
        print(f"===> Cookie 1 - {SIDValue}")
        print(f"===> Cookie 2 - {TSValue}")
        print(f"===> Cookie 3 - {CCValue}")
        print("")
        return cookie_dict

    except Exception as e:
        print(e)

cookie_dict = CookieScrapper()

global bard

try:    
    bard = BardCookies(cookie_dict=cookie_dict)
    Speak("*The verification of cookies has been successfully completed.*")
    print("*All processes have been completed successfully, and you now have the capability to employ Google Bard as a backend model.")
    print("")

except Exception as e:
    Speak("*The verification of cookies has encountered an issue and has not been successful.*")
    print("*This issue may arise due to the unsuccessful extraction of cookies from the extension.*")
    CookieScrapper()
    print(e)

def split_and_save_paragraphs(data, filename):

    try:

        paragraphs = re.split(r'(?<=[.!?])\s+', data)
        with open(filename, 'w') as file:
            for paragraph in paragraphs:
                file.write(paragraph + '\n\n')
        separator = ', '
        joined_string = separator.join(paragraphs[:5])
        return joined_string.replace("*", " ")
    
    except Exception as e:
        print(e)



 

def BardAi():
    global stop_flag
    while True:
        try:
            Speak("Enter the query Sir!")
            Question = TakeCommand_eng()
            RealQuestion = str(Question)

            if "close AI" in RealQuestion.lower() or "return to normal" in RealQuestion.lower() or "normal" in RealQuestion.lower():
                Speak("Closing Bard AI, converting to normal Sir!")
                break

            results = bard.get_answer(RealQuestion)['content']
            current_datetime = datetime.datetime.now()
            formatted_time = current_datetime.strftime("%H%M%S")
            filenamedate = str(formatted_time) + str(".txt")
            filenamedate = "Brain\\DataBase\\" + filenamedate

            links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', results)

            if links:
                Speak("Links in the response:")
                for link in links:
                    print(link)
            else:
                result_words = results.split(" ")
                result = " ".join(word.replace("*", " ") for word in result_words)


                if "Response Error: " in result:
                    print(result)
                else:
                    Speak(split_and_save_paragraphs(result, filenamedate))



        except Exception as e:
            print(e)


