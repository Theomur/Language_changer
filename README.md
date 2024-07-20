# Language_changer

 App that changes the language layout for your typed text

If you found yourself in a situation where you typed a lot of text in the wrong layout - just press the 

<Left_Ctrl + Left_Alt + Left_Shift + Right_Shift + Space> 

shortcut to trigger the script that will change text on different layout. It works by triggering <Ctrl + A> hotkey, cutting selected text and changing it using pregenerated dictionary. It has 2 dictionaries for ru-eng and eng-ru translation. Dictionaries are choosen automatically.

You can change the whole text in textbox or select only the text you need to change.

You can also turn this thing on and off in taskbar menu, restart the app in case of mailfunction or completely stop it.

---
# How to use this app:

- Launch Change_lang.py via code editor.

- Use .exe from /dist folder. 

# To build .EXE file:

- install [Python 3.12.4](https://www.python.org/downloads/release/python-3124/) (I used this version, you can install more recent one if you sure it won't broke anything).

- Download project and open it in any code editor.

- Create virtual environment:

```shell
py -m venv venv
```

- Activate virtual environment:

```shell
source venv/Scripts/activate
```

- Install requirements:

```shell
pip install -r requirements.txt
```

- type following command to generate the exe application:

```shell
pyinstaller Change_lang.spec
```

Go to the project folder in windows explorer, open /dist folder and copy or cut the /Change_lang folder to your desired destination.

You can also add it to windows autostartup so this app would always be with you.

You can also change On/Off icons in project root.

---

Enjoy ❤️
