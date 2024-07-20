import keyboard
from PIL import Image
import pyperclip
import pyautogui
import pystray
from pystray import MenuItem as item
import time
from LanguagesDics import eng_to_rus, rus_to_eng, ru_alph, en_alph


def TextNotSelected():
    clipboard_before = pyperclip.paste()
    time.sleep(0.7)
    pyautogui.hotkey("ctrl", "c")
    clipboard_after = pyperclip.paste()
    pyperclip.copy(clipboard_before)
    return clipboard_before == clipboard_after


def logic():
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
        norm_text += dictionary[enc_text[i]]
    keyboard.write(norm_text)


image = Image.open("Language_changer/icon.png")
icon = pystray.Icon("Language change", image, "Language change")
icon.menu = pystray.Menu(item("Quit", icon.stop))
icon.run()


keyboard.add_hotkey("left ctrl+left alt+right shift+left shift+space", logic)
