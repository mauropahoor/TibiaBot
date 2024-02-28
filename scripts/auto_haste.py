import pyautogui as pg
#py -m pip install pyautogui
import time
import dearpygui.dearpygui as dpg
from win32gui import GetWindowText, GetForegroundWindow

def auto_haste(sender):
    while dpg.get_value(sender):
        if 'tibia' in GetWindowText(GetForegroundWindow()).lower(): #Check if tibia is open
            try:
                pg.locateOnScreen('scripts/imgs/haste.png', confidence=0.9)
            except pg.ImageNotFoundException:
                pg.press(dpg.get_value('hotkey_haste'))
            time.sleep(0.15)