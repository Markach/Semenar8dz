import sqlite3

db = sqlite3.connect("details.db")
cursor=db.cursor()

# # Добавление данных
def add_film():
    menu = int(input("Нажмите 1, если хотите добавить фильм в картотеку, нужно добавить: \n1. Добавить  название фильма \n2. Жанр \n3. Страна \n4. Год выпуска \n5. Рейтинг \n6. Язык \n"))
    if menu == 1:
        title = input('Название фильма: ')
        genre = input('Жанр фильма: ')
        country = input('Страна: ')
        release_year= input('Год выпуска: ')
        audience_rating= input('Рейтинг: ')    
        language= input('Язык: ')     
    cursor.execute("SELECT COUNT(*) from films WHERE title = '"+  title +"'")
    result = cursor.fetchone()

    if int(result[0]) > 0:
        print('такой фильм есть в картотеке')                                 
    else:
        print(f'фильм {title} добавлен')                                              
        cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", (title, genre, country, release_year, audience_rating, language))
        db.commit()
# add_film()