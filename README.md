# Language_changer

Приложение для смены языковой раскладки вашего текста.

Если вы оказались в ситуации, когда набрали много текста в неправильной раскладке, просто нажмите сочетание клавиш:

<Left_Ctrl + Left_Alt + Left_Shift + Right_Shift + Space>

чтобы запустить скрипт, который изменит текст на другую раскладку. Оно работает так: выделяет через <Ctrl + A>, вырезает выделенный текст и меняет его с использованием предварительно созданного словаря. У него есть два словаря для перевода русско-английский и англо-русский. Словари выбираются автоматически.

Вы можете изменить весь текст в текстовом поле или выделить только тот текст, который нужно изменить.

Также вы можете включить и выключить приложение через меню в панели задач, перезапустить приложение в случае неисправности, настроить свою комбинацию клавиш или полностью остановить приложение.

---

# Как использовать это приложение:

Есть два способа запустить его. Для начала скачайте проект (Code, затем Download ZIP), после чего можете сделать одно из двух:

1. Используйте для запуска .exe из папки /dist/Change_lang. (вы также можете переместить папку Change_lang в любое место)
   
   ВНИМАНИЕ - копируйте всю папку Change_lang, а не только .EXE. Ему нужна папка _internal/ в той же директории для работы.

2. Запустите Change_lang.py через редактор кода. (В случае, если хотите отредактировать или отладить приложение)

После запуска .exe файла вы увидите Синий Глобус в вашей панели задач, что означает, что приложение работает.

Если кликнуть правой кнопкой мыши, вы увидите меню:

- Toggle (основной переключатель включения/выключения. Глобус розовый, когда приложение выключено)

- Hotkey setup (окно настройки, которое позволит вам установить свою комбинацию клавиш, если вам не нравится стандартная)

- Restart (перезапуск приложения)

- Quit (закрытие приложения)

---

# Приложение не работает

Это нормально, иногда оно немного капризное.

Просто перезапустите его несколько раз, скопируйте любой текст, попробуйте использовать комбинацию клавиш в текстовом поле. Также можно попробовать удерживать комбинацию клавиш несколько секунд, отпустить, скопировать текст и перезапустить приложение.

Когда вы перезапустите его несколько раз, оно должно заработать нормально.

---

# Как создать .EXE файл:

- Установите [Python 3.12.4](https://www.python.org/downloads/release/python-3124/) (Я использовал эту версию, можно установить более новую, если уверены, что ничего не сломается).

- Скачайте проект и откройте его в любом редакторе кода.

- Создайте виртуальное окружение:

```shell
py -m venv venv
```

- Активируйте виртуальное окружение:

```shell
source venv/Scripts/activate
```

- Установите зависимости:

```shell
pip install -r requirements.txt
```

- Введите следующую команду для создания exe приложения:

```shell
pyinstaller Change_lang.spec
```

Перейдите в папку проекта в проводнике Windows, откройте папку /dist и скопируйте или переместите папку /Change_lang в желаемое место.

Вы также можете добавить его в автозапуск Windows, чтобы приложение всегда было с вами.

Вы также можете изменить иконки Вкл/Выкл в корне проекта.

Наслаждайтесь ❤️

---

---

English readme:

---

# Language_changer

App that changes the language layout for your typed text

If you found yourself in a situation where you typed a lot of text in the wrong layout - just press the

<Left_Ctrl + Left_Alt + Left_Shift + Right_Shift + Space>

shortcut to trigger the script that will change text on different layout. It works by triggering <Ctrl + A> hotkey, cutting selected text and changing it using pregenerated dictionary. It has 2 dictionaries for ru-eng and eng-ru translation. Dictionaries are choosen automatically.

You can change the whole text in textbox or select only the text you need to change.

You can also turn this thing on and off in taskbar menu, restart the app in case of mailfunction, setup your own shortcut or completely stop the app.

---

# How to use this app:

there is 2 ways to launch it:

1. Use .exe from /dist/Change_lang folder. (you can also move Change_lang folder anywhere you want)
   
   CAUTION - copy the whole Change_lang folder, not the .EXE itself. It needs _internal/ folder in the same directory to operate/

2. Launch Change_lang.py via code editor. (In case you want to edit or debug the app)
   
   After you launched the .exe file, you will see the Blue Globe in your taskbar, which means the app is running.

if you riight click it - You will see the menu:

- Toggle (basic on/off switch. Gloge is pink when app is off)

- Hotkey setup (setup window that will allow you to setup your own hotkey if you dont like the default one)

- Restart (restarting the app)

- Quit (closing the app)

# App isn't working

Its okay, Its a little quirky sometimes.

just resturt it a bunch of times, copy any text, try to use the hotkey on a text field. you can also try to hold the hotkey for a few seconds, release it, copy text and restart the app.

when you restart it a few times - it should work just fine.

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

Enjoy ❤️
