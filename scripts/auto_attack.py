import pyautogui as pg
#py -m pip install pyautogui
import time
import dearpygui.dearpygui as dpg
from win32gui import GetWindowText, GetForegroundWindow

def auto_attack(sender):
    while dpg.get_value(sender):
        if 'tibia' in GetWindowText(GetForegroundWindow()).lower(): #Check if tibia is open
            try:
                battleList =  pg.locateOnScreen('imgs/battlelist.png', confidence=0.9)
                pg.locateOnScreen('imgs/battlelistEmpty.png', confidence=0.9) #If battle not empty, attack!
            except pg.ImageNotFoundException:
                creature_alive = True
                pg.press('space')
                while creature_alive:
                    try:
                        pg.locateOnScreen('imgs/battletargetAttack.png', region=(int(battleList.left), int(battleList.top), int(battleList.width), int(battleList.height + 21)), confidence=0.9)
                        time.sleep(0.5)
                    except:
                        creature_alive = False

def auto_spell(sender, spellsGroup: dict):
    hotkey = dpg.get_value('hotkey_spell')
    cooldown = spellsGroup[dpg.get_value('name_spell')] #Get the cooldown from dictionary

    i = 25
    while True:
        if 'tibia' in GetWindowText(GetForegroundWindow()).lower(): #Check if tibia is open
            try:
                battleList =  pg.locateOnScreen('imgs/battlelist.png', confidence=0.9)
                pg.locateOnScreen('imgs/battlelistEnd.png', region=(int(battleList.left), int(battleList.top), int(battleList.width + 14), int(battleList.height + i)), confidence=0.9)
                break
            except pg.ImageNotFoundException:
                i += 25
    while dpg.get_value(sender):
        if 'tibia' in GetWindowText(GetForegroundWindow()).lower(): #Check if tibia is open
            try:
                battleList =  pg.locateOnScreen('imgs/battlelist.png', confidence=0.9)
                test = pg.locateOnScreen('imgs/battletargetSpell.png', region=(int(battleList.left), int(battleList.top), int(battleList.width - 120), int(battleList.height + i)))
                #photo = pg.screenshot(region=(int(test.left), int(test.top), int(test.width), int(test.height)))
                #photo.show()
                #break
                pg.press(hotkey)
                time.sleep(cooldown)
            except pg.ImageNotFoundException:
                pass