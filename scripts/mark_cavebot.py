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

class StopHunt:
    def __init__(self): 
         self._stopHunt = False
      
    def get(self): 
        return self._stopHunt
      
    # setter method 
    def set(self, x):
        self._stopHunt = x 

stop_hunt = StopHunt()
def start_hunt(sender):
    stop_hunt.set(False)
    while keyboard.is_pressed('ESC') == False and stop_hunt.get() == False:
        if 'tibia' in GetWindowText(GetForegroundWindow()).lower(): #Check if tibia is open
            try:
                battleList =  pg.locateOnScreen('scripts/imgs/battlelist.png', confidence=0.9)
                pg.locateOnScreen('scripts/imgs/battlelistEmpty.png', confidence=0.9) #If battle not empty, attack!
                waypoint = pg.locateOnScreen(f'scripts/imgs/cavebot_waypoints/1.png', confidence=0.9)
                pg.moveTo(waypoint.left, waypoint.top)
                pg.click()
            except pg.ImageNotFoundException:
                pg.press('left')
                creature_alive = True
                while creature_alive:
                    try:
                        pg.locateOnScreen('scripts/imgs/battletargetAttack.png', region=(int(battleList.left), int(battleList.top), int(battleList.width), int(battleList.height + 21)), confidence=0.9)
                        time.sleep(0.5)
                    except:
                        creature_alive = False
                    