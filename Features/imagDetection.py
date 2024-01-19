from bardapi import BardCookies
import datetime
import pyperclip
import pyautogui
import webbrowser
from time import sleep
import json
import keyboard
import subprocess
import time

    

def CookieScrapper():
    chrome_path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Adjust the path based on your Chrome installation
    subprocess.Popen([chrome_path])
    time.sleep(2)  # Give Chrome some time to open

    webbrowser.open("https:\\bard.google.com\\chat")
    sleep(3)
    pyautogui.click(x=1595, y=92)
    sleep(3)
    pyautogui.click(x=1305, y=146)
    sleep(3)
    # pyautogui.click(x=1245, y=146)
    # sleep(3)
    keyboard.press_and_release('ctrl + w')

    data = pyperclip.paste()

    json_data = None  # Initialize json_data

    try:
        json_data = json.loads(data)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON data: {e}")

    # ... (other code)
    SID = "__Secure-1PSID"
    TS = "__Secure-1PSIDTS"
    CC = "__Secure-1PSIDCC"

    if json_data is not None:  # Check if json_data is assigned
        SIDValue = next((item for item in json_data if item["name"] == SID), None)
        TSValue = next((item for item in json_data if item["name"] == TS), None)
        CCValue = next((item for item in json_data if item["name"] == CC), None)

    

    # SIDValue = next((item for item in json_data if item["name"] == SID), None)
    # TSValue = next((item for item in json_data if item["name"] == TS), None)
    # CCValue = next((item for item in json_data if item["name"] == CC), None)

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

    return cookie_dict

cookie_dict = CookieScrapper()

bard = BardCookies(cookie_dict=cookie_dict)
# Text Modification Function -

def split_and_save_paragraphs(data, filename):
    paragraphs = data.split('\n\n')
    with open(filename, 'w') as file:
        file.write(data)
    data = paragraphs[:2]
    separator = ', '
    joined_string = separator.join(data)
    return joined_string

# Image Detection

while True:
    imagename = str(input("Enter The Image Name : "))
    image = open(imagename,'rb').read()
    bard = BardCookies(cookie_dict=cookie_dict)
    results = bard.ask_about_image('what is in the image?',image=image)['content']
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%H%M%S")
    filenamedate = str(formatted_time) + str(".txt")
    filenamedate = "Brain\\DATABASE\\" + filenamedate
    print(split_and_save_paragraphs(results, filename=filenamedate))

