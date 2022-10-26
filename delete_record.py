import sqlite3


db = sqlite3.connect("guid.db")
cursor = db.cursor()


def delete_record():
    id = int(input("Введи id для удаления записи: "))
    cursor.execute(f'SELECT * FROM guid WHERE Код = {id}')
    one = cursor.fetchmany()
    if not one:
        print("Такой записи не существует!")
    else:
        cursor.execute(f'DELETE FROM guid WHERE Код = {id}')
        print("Запись успешно удалена!")
        db.commit()