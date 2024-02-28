import dearpygui.dearpygui as dpg
import threading

from scripts.auto_attack import auto_attack
from scripts.auto_attack import auto_spell
from scripts.auto_loot import auto_loot

from scripts.auto_heal import auto_heal

from scripts.auto_eat import auto_eat

from scripts.auto_haste import auto_haste

from scripts.keyboard_cavebot import hunt
from scripts.keyboard_cavebot import stop_cavebot
from scripts.keyboard_cavebot import update_path
from scripts.keyboard_cavebot import record_file

from scripts.mark_cavebot import start_hunt

dpg.create_context()
dpg.create_viewport(title='CamposBot', width=500, height=600)

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
            dpg.add_button(label="Activate", callback=lambda: dpg.configure_item("autoheal_check_dialog", show=True))
            with dpg.popup(dpg.last_item(), mousebutton=dpg.mvMouseButton_Left, modal=True, tag="autoheal_check_dialog"):
                with dpg.texture_registry(show=False):
                    width, height, channels, data = dpg.load_image("scripts/imgs/healthbar.png")
                    dpg.add_static_texture(width=width, height=height, default_value=data, tag="health_image")
                with dpg.texture_registry(show=False):
                    width, height, channels, data = dpg.load_image("scripts/imgs/manabar.png")
                    dpg.add_static_texture(width=width, height=height, default_value=data, tag="mana_image")
                
                dpg.add_image("health_image")
                dpg.add_image("mana_image")
                dpg.add_text("Be sure that your health/mana bar is active\nand both health and mana are full when you click the Ok button!")
                with dpg.group(horizontal=True):
                    dpg.add_button(label="Ok", callback=lambda: threading.Thread(target=auto_heal, args=("auto_heal",)).start()) #Use threads to run more than 1 function at the same time

    with dpg.group(): #Utility group
        dpg.add_text("Utility:", bullet=True)
        with dpg.group(indent=25):
            with dpg.group(horizontal=True): #Auto Attack Group
                dpg.add_checkbox(tag="auto_attack", callback=lambda: threading.Thread(target=auto_attack, args=("auto_attack",)).start())
                dpg.add_text("Auto attack")
            with dpg.group(horizontal=True): #Auto Spell Group
                #Attack spell name + cooldown
                spells = {
                    "select cooldown": 2,
                    "sd/gfb/ava (2 seconds cooldown)": 2,
                    "exori (frigo/vis/tera/flam) (2 seconds cooldown)": 2,
                    "exori (4 seconds cooldown)": 4,
                    "exori gran (6 seconds cooldown)": 6,
                    "exevo vis hur (8 seconds cooldown)": 6,
                    "exori gran ico (30 seconds cooldown)": 30,
                    "exevo gran mas flam (40 seconds cooldown)": 40
                }
                dpg.add_checkbox(tag="auto_spell", callback=lambda: threading.Thread(target=auto_spell, args=("auto_spell", spells)).start())
                dpg.add_text("Auto spell:")
                dpg.add_combo(tag="hotkey_spell", items=hotkeys, width=45, default_value=hotkeys[2])
                dpg.add_combo(tag="name_spell", items=list(spells.keys()), width=130, default_value=list(spells.keys())[0])
            with dpg.group(horizontal=True): #Auto Eat Group
                dpg.add_checkbox(tag="auto_eat", callback=lambda: threading.Thread(target=auto_eat, args=("auto_eat",)).start())
                dpg.add_text("Auto eat:")
                dpg.add_combo(tag="hotkey_eat", items=hotkeys, width=45, default_value=hotkeys[9])
            with dpg.group(horizontal=True): #Auto Hur Group
                dpg.add_checkbox(tag="auto_hur", callback=lambda: threading.Thread(target=auto_haste, args=("auto_hur",)).start())
                dpg.add_text("Auto hur:")
                dpg.add_combo(tag="hotkey_haste", items=hotkeys, width=45, default_value=hotkeys[11])
            with dpg.group(horizontal=True): #Auto Loot Group
                dpg.add_checkbox(tag="auto_loot", callback=lambda: dpg.configure_item("autoloot_check_dialog", show=True))
                dpg.add_text("Auto loot")
                with dpg.popup(dpg.last_item(), mousebutton=dpg.mvMouseButton_Left, modal=True, tag="autoloot_check_dialog"):
                    with dpg.texture_registry(show=False):
                        width, height, channels, data = dpg.load_image("scripts/imgs/autolootTutorial.png")
                        dpg.add_static_texture(width=width, height=height, default_value=data, tag="tutorial_image")
                    dpg.add_image("tutorial_image")
                    dpg.add_text("Put your mouse pointer on your character and\npress CTRL button to activate autoloot!")
                    with dpg.group(horizontal=True):
                        dpg.add_button(label="Ok", callback=lambda: threading.Thread(target=auto_loot, args=("auto_loot",)).start())
    with dpg.group(): #Keyboard Cavebot
        dpg.add_text("Keyboard Cavebot:", bullet=True)
        with dpg.group(indent=25):
            with dpg.group(horizontal=True): #Start
                dpg.add_button(label="Start", callback=threading.Thread(target=hunt, args=("start_keyboard",)).start, width=50)
                dpg.add_button(label="Stop", callback=stop_cavebot, width=50)
            with dpg.group(horizontal=True): #Load and Record
                dpg.add_button(label="Load", callback=lambda: dpg.show_item("file_dialog_id"), width=50)
                dpg.add_button(label="Record", callback=lambda: dpg.configure_item("record_dialog_file", show=True), width=50)
                
                with dpg.popup(dpg.last_item(), mousebutton=dpg.mvMouseButton_Left, modal=True, tag="record_dialog_file"):
                        dpg.add_text("Write the name of your file:")
                        dpg.add_input_text(tag="record_name", default_value="huntTeste")
                        with dpg.group(horizontal=True): #Ok/Cancel group
                            dpg.add_button(label="Ok", callback=threading.Thread(target=record_file, args=("record",)).start)
                            dpg.add_button(label="Cancel", callback=lambda: dpg.configure_item("record_dialog_file", show=False))
            with dpg.group(horizontal=True): #Instructions
                dpg.add_button(label="Instructions", width=108)
    with dpg.group(): #Mark Cavebot
            dpg.add_text("Mark Cavebot:", bullet=True)
            with dpg.group(indent=25):
                with dpg.group(horizontal=True): #Start
                    dpg.add_button(label="Start", callback=lambda: threading.Thread(target=start_hunt, args=("start_markup",)).start(), width=50)
                    dpg.add_button(label="Stop", callback=stop_cavebot, width=50)
                with dpg.group(horizontal=True): #Instructions
                    dpg.add_button(label="Instructions", width=108)
                
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()