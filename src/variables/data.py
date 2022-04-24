BASE_DOMAIN = 'reddit.com'
BASE_URL = f'https://www.{BASE_DOMAIN}'
BASE_OAUTH_URL = f'https://oauth.{BASE_DOMAIN}'

# 1. Для работы с API необходим аккаунт на Reddit.
# 2. Создать приложение на https://www.reddit.com/prefs/apps/ .
#    При создании приложения выбрать тип: "script".
#    В поля "about url" и "redirect uri" вставить - http://localhost:8080
#    В поле "name" прописать название скрипта (название на Ваше усмотрение).
# 3. После создания приложения, необходимо открыть созданное приложение на редактирование...
#    Скопировать под текстом "personal use script" ID скрипта и вставить его в переменную SCRIPT_ID.
#    Скопировать рядом с текстом "secret" секретный ключ и вставить его в переменную SECRET_KEY.
#    Переменные USER_NAME и PASSWORD заполнить данными от аккаунта.
#    Переменную USER_AGENT можно оставить без изменений.

SCRIPT_ID = "BOllZlJh20kOfTmfiFtMbg"
SECRET_KEY = "WAhTEjq5wNKulX4OsK8OC4wLYicemg"
USER_NAME = "testov2022"
PASSWORD = "LSdHtp7tdUq8RTW"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
             "Chrome/100.0.4896.127 Safari/537.36 "
