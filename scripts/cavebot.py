import pyautogui as pg
#py -m pip install pyautogui
import keyboard
#pip install keyboard
from PIL import Image
import time
import numpy as np
#pip install numpy
import dearpygui.dearpygui as dpg
from win32gui import GetWindowText, GetForegroundWindow

def read_file(sender):
    file = open("hunts/teste.txt", "r")
    hunt = file.read()
    #while keyboard.is_pressed('ESC') == False:
    for i in range(len(hunt)):
        if hunt[i] == "w":
            pg.press("Up")
        elif hunt[i] == "a":
            pg.press("Left")
        elif hunt[i] == "s":
            pg.press("Down")
        elif hunt[i] == "d":
            pg.press("Right")
        time.sleep(0.2)