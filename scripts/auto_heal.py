import pyautogui as pg
import keyboard
import pytesseract as pt
from PIL import Image
import time

def auto_heal():
    pt.pytesseract.tesseract_cmd = r'..\tesseract\tesseract.exe'

    while keyboard.is_pressed('g') == False:
        healthBarLocation = pg.locateOnScreen('imgs\healthbar.png')
        healthBar = pg.screenshot(region=(healthBarLocation.left, healthBarLocation.top, healthBarLocation.width + 60, healthBarLocation.height))
        healthStatus = pt.image_to_string(healthBar)
        if(HealthStatus < 280):
            keyboard.release('F1')
        time.sleep(0.5)


keyboard.wait('h')
auto_heal()
