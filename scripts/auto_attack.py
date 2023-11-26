import pyautogui as pg
#py -m pip install pyautogui
import keyboard
#pip install keyboard
import time
import dearpygui.dearpygui as dpg

def auto_attack(sender, app_data):
    while dpg.get_value(sender):
        try:
            battleList =  pg.locateOnScreen('imgs/battlelist.png', confidence=0.9)
            pg.locateOnScreen('imgs/battlelistEmpty.png', confidence=0.9)
        except pg.ImageNotFoundException:
            creature_alive = True
            pg.press('space')
            while creature_alive:
                try:
                    pg.locateOnScreen('imgs/battletarget.png', region=(int(battleList.left), int(battleList.top), int(battleList.width), int(battleList.height + 21)), confidence=0.9)
                    time.sleep(0.5)
                except:
                    creature_alive = False
   