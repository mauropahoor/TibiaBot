import pyautogui as pg
import keyboard
from PIL import Image
import time
import numpy as np

def auto_heal(percentageHeal):

    healthBar = pg.locateOnScreen('imgs\healthbar.png', confidence=0.9)
    manaBar = pg.locateOnScreen('imgs\manabar.png', confidence=0.9)

    while keyboard.is_pressed('g') == False:
        try:
            red = get_red_pixels(pg.screenshot(region=(healthBar.left, healthBar.top, healthBar.width, healthBar.height)))
            
            if(red <= 0.16 * percentageHeal + 33): #Convert the percentage of healing to the pixels scale (0% --> 33 and 100% --> 49)
                keyboard.press('F1') #Use healing spell
            time.sleep(1)
        except:
            healthBar = pg.locateOnScreen('imgs\healthbar.png', confidence=0.9)
            
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



#keyboard.wait('h')
auto_heal(70)