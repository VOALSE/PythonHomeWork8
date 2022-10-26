import sqlite3


db = sqlite3.connect("guid.db")
cursor = db.cursor()


def add_record():
    city = input("Город: ")
    last_name = input("Фамилия: ")
    name = input("Имя: ")
    phone = input("Телефон: ")
    post = input("Должность: ")
    salary = input("Оклад: ")
    prize = input("Премия: ")
    guid = [(city, last_name, name, phone, post, salary, prize)]

    try:
        cursor.executemany('INSERT INTO guid VALUES(NULL,?,?,?,?,?,?,?)', guid)
        print("Данные успешно внесены\n")
        db.commit()
    except:
        print('Данные уже есть')
