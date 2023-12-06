import dearpygui.dearpygui as dpg
import threading
import string

from scripts.auto_attack import auto_attack

from scripts.auto_heal import auto_heal

from scripts.auto_haste import auto_haste

from scripts.cavebot import hunt
from scripts.cavebot import stop_cavebot
from scripts.cavebot import update_path
from scripts.cavebot import record_file


dpg.create_context()
dpg.create_viewport(title='MauroBot', width=600, height=400)

def get_file(sender, app_data):
    update_path(app_data['file_path_name']) #Update the path in cavebot to load the new hunt

with dpg.file_dialog(directory_selector=False, show=False, callback=get_file,  id="file_dialog_id", width=400 ,height=200):
    dpg.add_file_extension(".txt", color=(255, 0, 255, 255))

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
                dpg.add_button(label="Start", callback=threading.Thread(target=hunt, args=("start",)).start)
                dpg.add_button(label="Stop", callback=stop_cavebot)
            with dpg.group(horizontal=True): #Load and Record
                dpg.add_button(label="Load", callback=lambda: dpg.show_item("file_dialog_id"))
                dpg.add_button(label="Record", callback=lambda: dpg.configure_item("record_dialog_file", show=True))
                
                with dpg.popup(dpg.last_item(), mousebutton=dpg.mvMouseButton_Left, modal=True, tag="record_dialog_file"):
                        dpg.add_text("Write the name of your file:")
                        dpg.add_input_text(tag="record_name", default_value="huntTeste")
                        with dpg.group(horizontal=True): #Ok/Cancel group
                            dpg.add_button(label="Ok", callback=threading.Thread(target=record_file, args=("record",)).start)
                            dpg.add_button(label="Cancel", callback=lambda: dpg.configure_item("record_dialog_file", show=False))
                
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()