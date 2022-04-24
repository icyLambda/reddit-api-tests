# reddit-api-tests
Testing Reddit API...

#### Настройка для работы с Reddit API:
  1. Для работы с API необходим аккаунт на Reddit.
  2. Создать приложение на https://www.reddit.com/prefs/apps/ .  
     При создании приложения выбрать тип: "script".  
     В поля "about url" и "redirect uri" вставить - http://localhost:8080.  
     В поле "name" прописать название скрипта (название на Ваше усмотрение).  
  3. После создания приложения, необходимо открыть созданное приложение на редактирование...  
     Скопировать под текстом "personal use script" ID скрипта и вставить его в переменную SCRIPT_ID.  
     Скопировать рядом с текстом "secret" секретный ключ и вставить его в переменную SECRET_KEY.  
     Переменные USER_NAME и PASSWORD заполнить данными от аккаунта.  
     Переменную USER_AGENT можно оставить без изменений.  

#### Для запуска тестов:  
  1. Создать виртуальное окружение (можно в PyCharm через раздел Interpreter Settings или в терминале https://docs.python.org/3/library/venv.html).  
  2. Установить необходимые библиотеки командой в терминале: pip install -r requirements.txt.  

#### Локальный запуск из IDE PyCharm: 
  1. Установить папку src как Sources Root в контекстном меню.
  2. В меню Select Run/Debug Configuration выбрать Add Configuration или Edit Configurations.
  3. Создать новую конфигурацию или выбрать существующую: в диалоговом окне нажать кнопку Add New Configuration → Python.
  4. Настроить команду запуска: Module name: robot.run.
  5. Параметр Working Directory должен указывать на папку src.
  6. В поле Parameters ввести аргументы запуска тестов.

#### Пример конфигурации запуска теста:
```
--loglevel  
TRACE  
--variablefile  
variables/data.py  
--outputdir  
output  
--test  
"Testing Reddit API"  
tests
```

Лог автотеста будет доступен после выполнения скрипта по пути "**/reddit-api-tests/src/output/log.html**"
