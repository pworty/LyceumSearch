# Variables init
# Инициализация переменных
with open("settings.txt", "r") as f:
    data = f.readlines()
SHOW_TUTORIAL, DB_NAME, LANGUAGE = [d.split(' = ')[1].split('\n')[0] for d in
                                                   data]
SHOW_TUTORIAL = int(SHOW_TUTORIAL)
SECTION = 'ALL'
TYPE = 'ALL'