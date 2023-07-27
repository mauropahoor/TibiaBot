import pyautogui as pg
import keyboard
import pytesseract as pt
from PIL import Image
import time

def auto_heal():
    pt.pytesseract.tesseract_cmd = r'..\tesseract\tesseract.exe'

    while keyboard.is_pressed('g') == False:       
        healthBar = pg.locateOnScreen('imgs\healthbar.png', confidence=0.9)
        manaBar = pg.locateOnScreen('imgs\manabar.png', confidence=0.9)
        if(healthBar is None): #Check if your health is not full
            print("vida nao cheia")
            if(manaBar is None): #Check if your mana isn't empty
                keyboard.press('F1') #Use healing spell
            else:
                keyboard.press('F2') #Use mana potion
                keyboard.press('F1') #Use healing spell
        #healthBarLocation = pg.locateOnScreen('imgs\healthbar.png', confidence=0.7)
        #healthBar = pg.screenshot(region=(healthBarLocation.left + 100, healthBarLocation.top - 10, healthBarLocation.width + 50, healthBarLocation.height + 10))
        #healthBar.save(r'C:\Users\F8088819\Documents\PythonTeste\scripts\suavida.png')
        #healthStatus = pt.image_to_string(healthBar)
        #print(f"Sua vida é {healthStatus}")
        #time.sleep(0.5) 
        #Tentativa de saber o valor exato da vida


keyboard.wait('h')
auto_heal()