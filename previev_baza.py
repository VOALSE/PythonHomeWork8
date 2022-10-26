import sqlite3

db = sqlite3.connect("guid.db")
cursor = db.cursor()


def previev_baza():
    while True:
        user_choise = input('\nВыбери пункт меню:\
                        \n1 - Просмотр данных\
                        \n2 - Показать максимальный оклад\
                        \n3 - Показать средний оклад\
                        \n4 - Показать максимальную премию\
                        \n5 - Показать среднюю премию\
                        \n6 - Вернуться в предыдущее меню\
                        \nВведи пункт меню: ')
        if user_choise == "1":
            for i in  cursor.execute('SELECT * FROM guid'):
                print(*i)
            print()
        if user_choise == "2":
            cursor.execute('SELECT max(Оклад) FROM guid')
            print()
            print(f'Максимальный оклад = {round(cursor.fetchone()[0])}')
        if user_choise == "3":
            cursor.execute('SELECT avg(Оклад) FROM guid')
            print()
            print(f'Средний оклад = {round(cursor.fetchone()[0])}')
        if user_choise == "4":
            cursor.execute('SELECT max(Премия) FROM guid')
            print()
            print(f'Максимальная премия = {round(cursor.fetchone()[0])}')
        if user_choise == "5":
            cursor.execute('SELECT avg(Премия) FROM guid')
            print()
            print(f'Средняя премия = {round(cursor.fetchone()[0])}')
        elif user_choise == "6":
            print()
            break


    max = "SELECT max(Оклад) FROM guid"
    cursor.execute(max)
    print(f'Максимальный оклад = {cursor.fetchone()[0]}')