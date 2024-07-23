import os
import sys
import threading
import time
from tkinter import messagebox

import keyboard
import pyautogui
import pyperclip
import pystray
from LanguagesDics import en_alph, eng_to_rus, ru_alph, rus_to_eng
from PIL import Image
from pystray import MenuItem as item

kill_switch_on = True
default_shortcut = "left ctrl+left alt+right shift+left shift+space"
shortcut = ""

try:
    shortcut_file = open("shortcut.txt", "r+")
    filename = "shortcut.txt"
except Exception as e:
    try:
        shortcut_file = open("Language_changer/shortcut.txt", "r+")
        filename = "Language_changer/shortcut.txt"
    except Exception as e:
        shortcut_file = open("_internal/shortcut.txt", "r+")
        filename = "_internal/shortcut.txt"
shortcut_file.close()

with open(filename, "r+") as f:
    data = f.read()
    if data:
        shortcut = data
    else:
        shortcut = default_shortcut
        f.write(shortcut)


def toggle_app(icon):
    global kill_switch_on
    kill_switch_on = not kill_switch_on
    icon.icon = icon.icon_on if kill_switch_on else icon.icon_off


def restart_app():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def shortcut_setup():
    global shortcut

    result1 = messagebox.askokcancel(
        "Hotkey setup",
        f"Are you sure, that you want to change your hotkey for Language_change? Your current hotkey :\n{shortcut}",
    )

    if result1:
        while True:
            shortcut = ""
            recorded_keys = []

            def on_key_event(event):
                name = event.name
                if event.event_type == "down":
                    if event.scan_code == 42:
                        name = "left shift"
                    elif event.scan_code == 54:
                        name = "right shift"
                    elif event.scan_code == 56:
                        name = "left alt"
                    elif event.scan_code == 3640:
                        name = "right alt"
                    elif event.scan_code == 29:
                        name = "left ctrl"
                    elif event.scan_code == 3613:
                        name = "right ctrl"
                    if name not in recorded_keys and name != "esc":
                        recorded_keys.append(name)

            recorded_keys.clear()
            keyboard.hook(on_key_event)

            result2 = messagebox.showinfo(
                "Hotkey setup",
                "Please enter your hotkey sequence.\n(press buttons one by one, not all of them at the same time)\nPress ok when you finish",
            )
            if result2:
                keyboard.unhook_all()

            shortcut = "+".join(recorded_keys)

            result3 = messagebox.askyesno(
                "Hotkey setup",
                f"Your new hotkey is:\n{shortcut}\nAre you sure you want to save it?",
            )

            if result3:
                with open(filename, "w") as f:
                    f.write(shortcut)
                break
        restart_app()
    else:
        return


def stop_app():
    shortcut_file.close()
    os._exit(0)


def create_tray_icon():
    try:
        imageOn = Image.open("iconOn.png")
        imageOff = Image.open("iconOff.png")
    except Exception as e:
        try:
            imageOn = Image.open("Language_changer/iconOn.png")
            imageOff = Image.open("Language_changer/iconOff.png")
        except Exception as e:
            imageOn = Image.open("_internal/iconOn.png")
            imageOff = Image.open("_internal/iconOff.png")

    icon = pystray.Icon("Language change", imageOn, "Language change")
    icon.menu = pystray.Menu(
        item("Toggle", toggle_app, checked=lambda item: kill_switch_on),
        item("Hotkey setup", shortcut_setup),
        item("Restart", restart_app),
        item("Quit", stop_app),
    )
    icon.icon_on = imageOn
    icon.icon_off = imageOff
    icon.run()


tray_thread = threading.Thread(target=create_tray_icon, daemon=True)
tray_thread.start()


def TextNotSelected():
    clipboard_before = pyperclip.paste()
    time.sleep(0.7)
    pyautogui.hotkey("ctrl", "c")
    clipboard_after = pyperclip.paste()
    pyperclip.copy(clipboard_before)
    return clipboard_before == clipboard_after


def logic():
    if kill_switch_on:
        print("triggered")
        if TextNotSelected():
            pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "x")

        enc_text = pyperclip.paste()
        norm_text = ""
        dictionary = {}

        for i in range(0, len(enc_text)):
            if enc_text[i] in ru_alph and enc_text[i] not in en_alph:
                dictionary = rus_to_eng
                pyautogui.hotkey("win", "space")
                break
            elif enc_text[i] in en_alph and enc_text[i] not in ru_alph:
                dictionary = eng_to_rus
                pyautogui.hotkey("win", "space")
                break

        for i in range(0, len(enc_text)):
            try:
                norm_text += dictionary[enc_text[i]]
            except Exception as e:
                print(e)
                norm_text += enc_text[i]
        keyboard.write(norm_text)


keyboard.add_hotkey(shortcut, logic)
keyboard.wait()
