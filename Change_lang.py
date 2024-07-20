import time

import keyboard
import pyautogui
import pyperclip

# import pystray
from LanguagesDics import en_alph, eng_to_rus, ru_alph, rus_to_eng

# from PIL import Image
# from pystray import MenuItem as item

# try:
#     image = Image.open("icon.png")
# except Exception as e:
#     try:
#         image = Image.open("Language_changer/icon.png")
#     except Exception as e:
#         image = Image.open("_internal/icon.png")


# icon = pystray.Icon("Language change", image, "Language change")
# icon.menu = pystray.Menu(item("Quit", icon.stop))
# icon.run()


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


keyboard.add_hotkey("left ctrl+left alt+right shift+left shift+space", logic)
keyboard.wait("esc")
