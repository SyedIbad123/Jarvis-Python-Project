from Features.clubui import Ui_SECRET
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QThread
import pyttsx3
import speech_recognition as sr
import os
import sys
import datetime
import random
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExe()

    def TakeCommand_eng(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print(": Recognizing...")
            self.query = r.recognize_google(audio, language="en-in")
            print(f"Your Command : {self.query}\n")
        except:
            print("Say that again")
            return ""
        return self.query.lower()

    def TaskExe(self):
        def play_specific_song(song_name):
            music_dir = 'C:\\Users\\User\\Music'
            song_path = os.path.join(music_dir, song_name)
            os.startfile(song_path)

        while True:
            self.query = self.TakeCommand_eng()
            if "wake up" in self.query:
                from Features import greet
                import importlib
                importlib.reload(greet)
                greet.Greet()

                while True:
                    self.query = self.TakeCommand_eng()
                    if "go to sleep" in self.query:
                        Speak("Ok sir, you can call me anytime")
                        break
                    elif "hello" in self.query:
                        Speak("Hello Sir! How are you")
                    elif "thank you" in self.query or "thank" in self.query:
                        Speak("you are welcome, Sir")

                    elif "bard" in self.query or "AI" in self.query or "ai" in self.query:
                        Speak("Converting Sir! ")
                        from Features.Bard import BardAi
                        BardAi()
                        Speak("Bard Task Completed, Sir")
                    
                    elif "time batao" in self.query or "time" in self.query:
                        Time = datetime.datetime.now().strftime("%H:%M:%S")
                        Speak(f"The current time is {Time}")

                    elif any(word in self.query for word in ["my location", "location", "current location"]):
                        from Features.Features import myloc
                        myloc(self.query)

                    elif "shutdown system" in self.query or "shutdown computer" in self.query:
                        Speak("Are you sure you want to shut down?")
                        shutdown = input("do you wish to shutdown your computer (yes/no)")
                        if shutdown == "yes":
                            os.system("shutdown /s /t 1")
                        elif shutdown == 'no':
                            break

                    elif "take screenshot" in self.query or "screenshot" in self.query:
                        import pyautogui
                        screenshot = "ss.jpg"
                        im = pyautogui.screenshot()
                        im.save(screenshot)
                        Speak("successfully done, sir")
                        try:
                            os.startfile(screenshot)
                        except Exception as e:
                            print(e)

                    elif "google" in self.query or "Google" in self.query:
                        from Features.Features import GoogleSearch
                        GoogleSearch(self.query)
                    elif "open youtube" in self.query or "open YouTube" in self.query:
                        webbrowser.open("https://www.youtube.com")
                    elif "open facebook" in self.query or "open Facebook" in self.query:
                        webbrowser.open("https://www.facebook.com")
                    elif "open whatsapp" in self.query or "open WhatsApp" in self.query:
                        webbrowser.open("https://web.whatsapp.com/")
                    elif "open instagram" in self.query or "open Intagram" in self.query:
                        webbrowser.open("https://www.instagram.com")
                  
                    elif "play aadat" in self.query or "aadat chala do" in self.query:
                        play_specific_song("E:\\songs\\Aadat_ Atif Aslam.mp3")

                    elif "play alone" in self.query or "play alone by alan walker" in self.query:
                        play_specific_song("E:\\songs\\Alone,Pt.II.mp3")
                    
                    elif "play faded" in self.query or "play faded by alan walker" in self.query:
                        play_specific_song("E:\\songs\\Alan Walker - Faded (64 kbps).mp3")

                    elif "play random music" in self.query or "koi bhi music chala do" in self.query:
                        music_dir = 'E:\\songs'
                        files = os.listdir(music_dir)
                        mp3_files = [f for f in files if f.endswith('.mp3')]
                        random.shuffle(mp3_files)
                        rand_file = mp3_files[0]
                        os.startfile(os.path.join(music_dir, rand_file))

                    elif "open" in self.query:
                        from Features.open_and_close_apps import openwebapp
                        openwebapp(self.query)
                    elif "close" in self.query:
                        from Features.open_and_close_apps import closeapp
                        closeapp(self.query)

                    elif "terminate" in self.query:
                        exit()

startFunction = MainThread() 

class SECRET_Start(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.club_ui = Ui_SECRET()
        self.club_ui.setupUi(self)

        self.club_ui.pushButton.clicked.connect(self.startFunc)
        self.club_ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):
        self.club_ui.movie_1 = QtGui.QMovie("images\\Iron_Template_1.gif")
        self.club_ui.gif_1.setMovie(self.club_ui.movie_1)
        self.club_ui.movie_1.start()

        self.club_ui.movie_2 = QtGui.QMovie("images\\Earth.gif")
        self.club_ui.gif_2.setMovie(self.club_ui.movie_2)
        self.club_ui.movie_2.start()

        self.club_ui.movie_3 = QtGui.QMovie("images\\Code_Template.gif")
        self.club_ui.gif_3.setMovie(self.club_ui.movie_3)
        self.club_ui.movie_3.start()

        startFunction.start()


if __name__ == "__main__":
    Gui_App = QtWidgets.QApplication(sys.argv)
    Gui_CLUB = SECRET_Start()
    Gui_CLUB.show()
    sys.exit(Gui_App.exec_())
