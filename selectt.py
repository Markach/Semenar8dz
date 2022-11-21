import sqlite3

db = sqlite3.connect("details.db")
cursor=db.cursor()
# Выборка данных
#  жанр
def select_genre():
    variable = str.lower(input('Введите жанр, из которого хотите выбирать '))
    cursor.execute("SELECT * from films   WHERE genre = '"+  variable +"'")
    result = cursor.fetchone()
    if result == None:
        print('Нет такого жанра в картотеке!') 
    else:
        res = cursor.fetchall()
        cursor.execute("SELECT * from films   WHERE genre = '"+  variable +"'")

        print(res)
# select_genre()

# название фильма
def select_film():
    variable = str.capitalize(input('Введите название фильма '))
    cursor.execute("SELECT * from films   WHERE title = '"+  variable +"'")
    result = cursor.fetchone()

    if result == None:
        print('Нет такого фильма в картотеке!')   
    else:
        cursor.execute("SELECT * from films   WHERE title= '"+ variable +"'")
        db.commit()
    print(result)
# select_film()

# язык 
def select_language():
    variable = str.lower(input('Введите язык, из котором хотите выбрать фильм '))
    cursor.execute("SELECT * from films   WHERE language = '"+  variable +"'")
    result = cursor.fetchone()

    if result == None:
        print('Нет фильма на таком языке в картотеке!')   
    else:
        res = cursor.fetchall()
        cursor.execute("SELECT * from films   WHERE language= '"+ variable +"'")
        db.commit()
        print(res)
# select_language()

def select_all():
    cursor.execute("SELECT * from films ")
    result = cursor.fetchall()
    print(result)

# select_all()    