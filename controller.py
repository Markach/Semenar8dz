import delete_film as de
import insert_film as ins
import selectt as s
import update_rating as up


def choose():
    while True:
        print('''\n1. Посмотреть всю фильмотеку; \n2. Выбрать по жанру(комедия, боевик, ужасы, драма); \n3. Выбрать по названию фильма; \n4. Выбрать по языку; \n5. Удалить данные из фильмотеки по названию фильма; \n6. Добавление фильма; \n7. Обновление рейтинга фильма; \n8. Выход''')
        choice = input('\nВыберите вариант и введите цифру: ')
        if choice == '1':
            s.select_all()
        if choice == '2':
            s.select_genre()
        if choice == '3':
            s.select_film()
        if choice == '4':
            s.select_language()
        if choice == '5':
            de.del_film() 
        if choice == '6':
            ins. add_film()
        if choice == '7':
            up. update_rating()      
        if choice == '8':
            print('\nДо скорой встречи!\n')
            break