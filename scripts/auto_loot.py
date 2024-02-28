import pyautogui as pg
#py -m pip install pyautogui
import time
import dearpygui.dearpygui as dpg
from win32gui import GetWindowText, GetForegroundWindow
import keyboard

def auto_loot(sender):
    dpg.configure_item("autoloot_check_dialog", show=False)
    keyboard.wait('CTRL')
    x, y =pg.position()
    while dpg.get_value(sender):
        if 'tibia' in GetWindowText(GetForegroundWindow()).lower(): #Check if tibia is open
            try:
                battleList =  pg.locateOnScreen('scripts/imgs/battlelist.png', confidence=0.9)
                pg.locateOnScreen('scripts/imgs/battlelistEmpty.png', confidence=0.9)
            except pg.ImageNotFoundException:
                time.sleep(0.1)
                creature_alive = True
                while creature_alive:
                    try:
                        pg.locateOnScreen('scripts/imgs/battletargetAttack.png', region=(int(battleList.left), int(battleList.top), int(battleList.width), int(battleList.height + 21)), confidence=0.9)
                        time.sleep(0.5)
                    except:
                        loot_macro(x, y)
                        creature_alive = False

def loot_macro(x, y):
    wait = 0
    pixels = 60

    pg.click(button='right', x = x + pixels, y = y)
    time.sleep(wait)
    pg.click(button='right', x = x + pixels, y = y + pixels)
    time.sleep(wait)
    pg.click(button='right', x = x, y = y + pixels)
    time.sleep(wait)
    pg.click(button='right', x = x - pixels, y = y + pixels)
    time.sleep(wait)
    pg.click(button='right', x = x - pixels, y = y)
    time.sleep(wait)
    pg.click(button='right', x = x - pixels, y = y - pixels)
    time.sleep(wait)
    pg.click(button='right', x = x, y = y - pixels)
    time.sleep(wait)
    pg.click(button='right', x = x + pixels, y = y - pixels)  