import sqlite3

db = sqlite3.connect("details.db")
cursor=db.cursor()

# # Изменение данных
def update_rating():
    variable = input('Введите название фильма, которому нужно изменить рейтинг: ')
    cursor.execute("SELECT COUNT(*) from films WHERE title = '"+  variable +"'")
    result = cursor.fetchone()

    if int(result[0]) == 0:
        print(f'фильма {variable} нет в картотеке! ')
    else:
        new = input('Введите новый рейтинг: ')
        cursor.execute("UPDATE films SET audience_rating = '"+ new +"' WHERE title= '"+ variable +"'")
        print('рейтинг успешно изменен') 
        db.commit()

# update_rating()        