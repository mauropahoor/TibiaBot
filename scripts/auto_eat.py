import pyautogui as pg
#py -m pip install pyautogui
import time
import dearpygui.dearpygui as dpg
from win32gui import GetWindowText, GetForegroundWindow

def auto_eat(sender):
    while dpg.get_value(sender):
        if 'tibia' in GetWindowText(GetForegroundWindow()).lower(): #Check if tibia is open
            try:
                pg.locateOnScreen('imgs/hungry.png', confidence=0.9) #If hungry is active, eat, else wait
                pg.press(dpg.get_value('hotkey_eat'))
            except pg.ImageNotFoundException:
                pass
            time.sleep(0.5)