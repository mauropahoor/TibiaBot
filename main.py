import dearpygui.dearpygui as dpg
import threading

from scripts.auto_attack import auto_attack
from scripts.auto_heal import auto_heal
from scripts.auto_haste import auto_haste
from scripts.cavebot import read_file

dpg.create_context()
dpg.create_viewport(title='MauroBot', width=600, height=400)

with dpg.window(tag="Primary Window"):
    hotkeys = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"]

    with dpg.group(): #Healing Group
        dpg.add_text("Healing:", bullet=True)
        with dpg.group(indent=25):
            with dpg.group(horizontal=True): #Health group
                dpg.add_text("Life:")
                dpg.add_input_text(tag="heal_value", default_value=80, width=25)
                dpg.add_text("%")
                dpg.add_combo(tag="hotkey_health", items=hotkeys, width=45, default_value=hotkeys[0])
            with dpg.group(horizontal=True): #Mana Group
                dpg.add_text("Mana:")
                dpg.add_input_text(tag="mana_value", default_value=50, width=25)
                dpg.add_text("%")
                dpg.add_combo(tag="hotkey_mana", items=hotkeys, width=45, default_value=hotkeys[1])
            dpg.add_button(label="Activate", callback=threading.Thread(target=auto_heal, args=("auto_heal",)).start) #Use threads to run more than 1 function at the same time

    with dpg.group(): #Utility group
        dpg.add_text("Utility:", bullet=True)
        with dpg.group(indent=25):
            with dpg.group(horizontal=True): #Auto Attack Group
                dpg.add_checkbox(tag="auto_attack", callback=threading.Thread(target=auto_attack, args=("auto_attack",)).start)
                dpg.add_text("Auto attack")
            with dpg.group(horizontal=True): #AutoHur Group
                dpg.add_checkbox(tag="auto_hur", callback=threading.Thread(target=auto_haste, args=("auto_hur",)).start)
                dpg.add_text("Autohur:")
                dpg.add_combo(tag="hotkey_haste", items=hotkeys, width=45, default_value=hotkeys[11])

    with dpg.group(): #Cavebot
        dpg.add_text("Cavebot:", bullet=True)
        with dpg.group(indent=25):
            with dpg.group(horizontal=True): #Start
                dpg.add_button(label="Start", callback=read_file)
                dpg.add_button(label="Stop", callback=threading.Thread(target=auto_heal, args=("auto_heal",)).start)
            with dpg.group(horizontal=True): #AutoHur Group
                dpg.add_button(label="Load", callback=threading.Thread(target=auto_heal, args=("auto_heal",)).start)
                dpg.add_button(label="Record", callback=threading.Thread(target=auto_heal, args=("auto_heal",)).start)
                
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()