from menu import input_choices_main
import sqlite3


def guid():
    db = sqlite3.connect("guid.db")
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS guid
        (
        Код INTEGER PRIMARY KEY AUTOINCREMENT,
        Город TEXT,
        Фамилия TEXT,
        Имя TEXT,
        Телефон TEXT,
        Должность TEXT,
        Оклад INTEGER,
        Премия INTEGER
    )''')
    

guid()


input_choices_main()