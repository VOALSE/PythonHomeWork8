import sqlite3


db = sqlite3.connect("guid.db")
cursor = db.cursor()


def change_record():
    while True:
        user_choise = input('\nВыбери пункт меню:\
                        \n1 - Изменение данных\
                        \n2 - Вернуться в предыдущее меню\
                        \nВведи пункт меню: ')
        if user_choise == "1":
            print()
            id = int(input("Введи id для изменения записи: "))
            cursor.execute(f'SELECT * FROM guid WHERE Код = {id}')
            one = cursor.fetchmany()
            if not one:
                print("Такой записи не существует!")
            else:
                cursor.execute(f'SELECT * FROM guid WHERE Код = {id}')
                j = cursor.fetchone()
                print(j)
                m = input('Введи название столбца для внесения изменений: ')
                n = input(f'Укажи новые данные для столбца "{m}": ')
                print(n)
                cursor.execute(f'UPDATE guid SET {m} = "{n}" WHERE Код = {id}')
                db.commit()
                print("Данные изменены!")
        elif user_choise == "2":
            print()
            break
        