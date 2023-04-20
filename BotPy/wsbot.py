import pyautogui, webbrowser
from time import sleep

webbrowser.open("https://web.whatsapp.com/send?phone=+(number)")
sleep(16)

"""
pyautogui.typewrite("Hotel Oscar Lima Alpha, Charlie Oscar Mike Oscar, Echo Sierra Tango Alpha Sierra??\n November Uniform November Charlie Alpha / Echo November / Mike India / Lima India Victor Echo / Lima Alpha Golf Alpha / Sierra Tango / Charlie Oscar November / Tango Alpha November / Lima India November Delta Oscar Sierra / Lima Oscar Sierra / Tango Yankee Oscar Uniform Sierra / Tango Uniform Yankee Oscar Sierra ")
pyautogui.press("enter")
"""
#Spam

with open ("spam.txt", "r") as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
