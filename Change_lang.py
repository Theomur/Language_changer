import os
import sys
import threading
import time

import keyboard
import pyautogui
import pyperclip
import pystray
from PIL import Image
from pystray import MenuItem as item

from LanguagesDics import en_alph, eng_to_rus, ru_alph, rus_to_eng

kill_switch_on = True
default_shortcut = "left ctrl+left alt+right shift+left shift+space"


def toggle_app(icon):
    global kill_switch_on
    kill_switch_on = not kill_switch_on
    icon.icon = icon.icon_on if kill_switch_on else icon.icon_off


def restart_app():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def stop_app():
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
    print("triggered")
    if kill_switch_on:
        if TextNotSelected():
            pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "x")

        enc_text = pyperclip.paste()
        norm_text = ""
        dictionary = {}

        for i in range(0, len(enc_text)):
            if enc_text[i] in ru_alph and enc_text[i] not in en_alph:
                dictionary = rus_to_eng
                break
            elif enc_text[i] in en_alph and enc_text[i] not in ru_alph:
                dictionary = eng_to_rus
                break

        for i in range(0, len(enc_text)):
            try:
                norm_text += dictionary[enc_text[i]]
            except Exception as e:
                norm_text += enc_text[i]
        keyboard.write(norm_text)


shortcut = "ctrl+alt+shift"  # ToDo - make it customisable

keyboard.add_hotkey(default_shortcut, logic)
keyboard.wait()
