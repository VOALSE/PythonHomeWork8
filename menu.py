from change_record import change_record
from previev_baza import previev_baza
from add_record import add_record
from delete_record import delete_record


def input_choices_main():
    while True:
        user_choise = input('\nОсновное меню:\
                            \n1 - Изменение данных\
                            \n2 - Просмотр данных\
                            \n3 - Выход\
                            \nВыбери пункт меню: ')
        if user_choise == "1":
            print()
            menu_changes()
        elif user_choise == "2":
            print()
            previev_baza()
        elif user_choise == "3":
            print()
            print("Спасибо, что воспользовались моей программой!")
            break


def menu_changes():
    while True:
        user_choise = input('Меню редактирования базы данных\
                            \n1 - Посмотреть базу\
                            \n2 - Добавить запись\
                            \n3 - Изменить запись\
                            \n4 - Удалить запись\
                            \n5 - Вернуться в основное меню\
                            \nВыбери пункт меню: ')
        if user_choise == "1":
            print()
            previev_baza()
        elif user_choise == "2":
            print()
            add_record()
        elif user_choise == "3":
            print()
            change_record()
        elif user_choise == "4":
            print()
            delete_record()
        elif user_choise == "5":
            print()
            break
