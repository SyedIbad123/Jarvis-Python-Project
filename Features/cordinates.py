import pyautogui
import keyboard
import pyperclip
from time import sleep
import webbrowser

# # webbrowser.open("https:\\bard.google.com\\chat")
# sleep(8)
# print(pyautogui.position())


try:
    while True:
        # Get the current mouse cursor position
        x, y = pyautogui.position()

        # Print the coordinates
        print(f"X: {x}, Y: {y}")
except KeyboardInterrupt:
    print("\nProgram terminated by user.")