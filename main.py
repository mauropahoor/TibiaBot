import dearpygui.dearpygui as dpg
from scripts.auto_attack import auto_attack
from scripts.auto_heal import auto_heal
import dearpygui.demo as demo

dpg.create_context()
dpg.create_viewport(title='MauroBot', width=600, height=400)

def button_callback(sender, app_data, user_data):
    print(f"sender is: {sender}")
    print(dpg.get_value('hotkey'))
    print(f"user_data is: {user_data}")

with dpg.window(tag="Primary Window"):
    dpg.add_text("Healing:")
    dpg.add_text("Life: %")
    dpg.add_input_text(tag="heal_value", default_value=80)
    hotkeys = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"]
    dpg.add_listbox(tag="hotkey_health", items= hotkeys)
    dpg.add_text("Mana: %")
    dpg.add_input_text(tag="mana_value", default_value=50)
    dpg.add_listbox(tag="hotkey_mana", items=hotkeys)
    dpg.add_button(label="Activate", callback=auto_heal)

    dpg.add_text("Auto attack:")
    dpg.add_checkbox(tag="auto_attack", callback=auto_attack)

    dpg.add_button(label="Print to Terminal", callback=button_callback, user_data="Some Data")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()