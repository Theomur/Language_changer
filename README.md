# Language_changer

 App that changes the language layout for your typed text

If you found yourself in a situation where you typed a lot of text in the wrong layout - just press the 

<Left_Ctrl + Left_Alt + Left_Shift + Right_Shift + Space> 

shortcut to trigger the script that will change text on different layout. It works by triggering <Ctrl + A> hotkey, cutting selected text and changing it using pregenerated dictionary. It has 2 dictionaries for ru-eng and eng-ru translation. Dictionaries are choosen automatically.

You can change the whole text in textbox or select only the text you need to change.

You can also turn this thing on and off in taskbar menu, restart the app in case of mailfunction or completely stop it.

# To download this project locally:

1. Click on green button "Code"

2. Then "Download ZIP"

3. Unzip the project to wherever you like
   
   ![](https://github.com/Theomur/Language_changer/blob/main/Readme%20images/ZIP.png)

Now you can look around files and do whatever you would like with them. You don't need anything else for that.

---

# To turn this project to .EXE file and actually use it:

I will explain how to do it on Windows 10/11 using VScode

- install [Python 3.12.4](https://www.python.org/downloads/release/python-3124/) to your system if you haven't done it yet (I used this version, you can install more recent one if you sure it won't broke anything). To do it you need to scroll down to Files section and choose recommended option.

<img title="" src="https://github.com/Theomur/Language_changer/blob/main/Readme%20images/Python.png" alt="" width="520">

- Download project and open it in any code editor (VScode in my case). It will underscore a lot of things but we will solve it in a sec.

- Open terminal using buttons on top of VScode or use <Ctrl+Shift+`> shortcut

![](https://github.com/Theomur/Language_changer/blob/main/Readme%20images/Terminal.png)

- In opened terminal check that your path (yellow text) is the same that you expect

- Now create virtual environment using command:

```shell
py -m venv venv
```

- then activate your new venv using command:

```shell
source venv/Scripts/activate
```

You should now have (venv) text under executed commands:

<img title="" src="https://github.com/Theomur/Language_changer/blob/main/Readme%20images/VENV.png" alt="" width="451">

- In activated venv type following command to get all packages you need to execute this code:

```shell
pip install -r requirements.txt
```

VScode should request to change your workspace folder in bottom right corner. It will change interpreter to the one with all dependences.

![](https://github.com/Theomur/Language_changer/blob/main/Readme%20images/PIP%20install.png)

If it didn't happened - change it yourself by clicking on python version I underscored and changing it to reccomended:

![](https://github.com/Theomur/Language_changer/blob/main/Readme%20images/PIP%20install%20but%20no.png)

Now your version should look like this:

![](https://github.com/Theomur/Language_changer/blob/main/Readme%20images/PY%20venv.png)

If you will launch this code it should work but to make a .EXE file we should do few more steps:

- type following command to generate the exe application:

```shell
pyinstaller Change_lang.spec
```

It will create /dist and /build folders in the project.

Go to the project folder in windows explorer, open /dist folder and copy or cut the /Change_lang folder to your desired destination, where you have all your programs.

You can also add it to windows autostartup in task manager so this app would be with you no matter what.

---

Enjoy ❤️
