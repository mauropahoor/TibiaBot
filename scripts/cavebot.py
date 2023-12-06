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

class Directory:
    def __init__(self, path = ""): 
         self._path =  path
      
    def get(self): 
        return self._path 
      
    # setter method 
    def set(self, x):
        self._path = x 

class StopHunt:
    def __init__(self): 
         self._stopHunt = False
      
    def get(self): 
        return self._stopHunt
      
    # setter method 
    def set(self, x):
        self._stopHunt = x 

stop_hunt = StopHunt()
path = Directory()
def hunt(sender):
    stop_hunt.set(False)

    file = open(f"{path.get()}", "r")
    hunt = file.read()
    while keyboard.is_pressed('ESC') == False and stop_hunt.get() == False:
        if 'tibia' in GetWindowText(GetForegroundWindow()).lower(): #Check if tibia is open
                i = 0
                while i != len(hunt):
                    #and (keyboard.is_pressed("ESC") == False and stop_hunt.get() == False)
                    try:
                        pg.locateOnScreen('imgs/battlelistEmpty.png', confidence=0.9)
                        if hunt[i] == "w":
                            pg.press("Up")
                        elif hunt[i] == "a":
                            pg.press("Left")
                        elif hunt[i] == "s":
                            pg.press("Down")
                        elif hunt[i] == "d":
                            pg.press("Right")
                        i += 1
                        time.sleep(0.2)
                    except pg.ImageNotFoundException:
                        pass

def stop_cavebot(sender):
    stop_hunt.set(True)

def update_path(app_data):
    path.set(app_data)

def record_file(sender):
    dpg.configure_item("record_dialog_file", show=False)
    file = open(f"hunts/{dpg.get_value('record_name')}.txt", "w")
    while keyboard.is_pressed('ESC') == False:
        if 'tibia' in GetWindowText(GetForegroundWindow()).lower(): #Check if tibia is open
            if keyboard.is_pressed("Up") or keyboard.is_pressed("W"):
                file.write("w")
            elif keyboard.is_pressed("Left") or keyboard.is_pressed("A"):
                file.write("a")
            elif keyboard.is_pressed("Right") or keyboard.is_pressed("D"):
                file.write("d")
            elif keyboard.is_pressed("Down") or keyboard.is_pressed("S"):
                file.write("s")
            time.sleep(0.3)    