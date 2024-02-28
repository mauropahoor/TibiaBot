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

def auto_heal(sender):
    dpg.configure_item("autoheal_check_dialog", show=False)
    healthBar = pg.locateOnScreen('scripts\imgs\healthbar.png', confidence=0.9)
    i = 0

    while keyboard.is_pressed('ESC') == False:
        if 'tibia' in GetWindowText(GetForegroundWindow()).lower(): #Check if tibia is open
            percentageHeal = int(dpg.get_value('heal_value')) #Get the heal percentage from the input
            percentageMana = int(dpg.get_value('mana_value')) #Get the mana percentage from the input

            hotkeyHealth = dpg.get_value('hotkey_health') #Get the hotkey to be used with health
            hotkeyMana = dpg.get_value('hotkey_mana') #Get the hotkey to be used with mana

            try:
                health = get_red_pixels(pg.screenshot(region=(int(healthBar.left), int(healthBar.top), int(healthBar.width), int(healthBar.height))))
                mana = get_blue_pixels(pg.screenshot(region=(int(healthBar.left), int(healthBar.top + 13), int(healthBar.width), int(healthBar.height))))
                

                if(i == 0): #Get the max value of the function
                    healthMax = health
                    manaMax = mana #mana <= ((manaMax-42)/100) * percentageHeal + 42
                    i += 1
                #print(f"Vida {red}\nCalculo: {((redMax-33)/100) * percentageHeal + 33}")
                if(health <= ((healthMax-33)/100) * percentageHeal + 33): #Convert the percentage of healing to the pixels scale (0% --> 33 and 100% --> redMax)
                    pg.press(f'{hotkeyHealth}') #Use healing spell
                if(mana <= ((manaMax-42)/100) * percentageMana + 42):
                    pg.press(f'{hotkeyMana}')
                time.sleep(1)
            except pg.ImageNotFoundException:
                healthBar = pg.locateOnScreen('scripts\imgs\healthbar.png', confidence=0.9)
                
            #if(healthBar is None): #Check if your health is not full
            #    print("vida nao cheia")
            #    if(manaBar is None): #Check if your mana isn't empty
            #        keyboard.press('F1') #Use healing spell
            #    else:
            #        keyboard.press('F2') #Use mana potion
            #        keyboard.press('F1') #Use healing spell
            #Script para healar a vida basico.
        
def get_red_pixels(healthbar_screenshot):
    arr_list= np.array(healthbar_screenshot)
    r=g=b=0
    for row in arr_list: #Count all of the red pixels in the screen
        for item in row:
            r=r+item[0]
            g=g+item[1]
            b=b+item[2]  
    total=r+g+b
    return r/total*100 #Get red percentage of the pixels (life amount)

def get_blue_pixels(manabar_screenshot):
    arr_list= np.array(manabar_screenshot)
    r=g=b=0
    for row in arr_list: #Count all of the blue pixels in the screen
        for item in row:
            r=r+item[0]
            g=g+item[1]
            b=b+item[2]  
    total=r+g+b
    return b/total*100 #Get blue percentage of the pixels (mana amount)
