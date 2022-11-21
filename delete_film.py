import sqlite3

db = sqlite3.connect("details.db")
cursor=db.cursor()

# # Удаление данных по названию фильма
def del_film():
    
    variable = str.capitalize(input('Введите название фильма'))
    cursor.execute("SELECT COUNT(*) from films WHERE title = '"+  variable+"'")
    result = cursor.fetchone()

    if int(result[0]) == 0:
        print(f'фильма {variable} нет в картотеке! ')                        
    else:
        print(f'фильм {variable} удален')                                                            
        cursor.execute("DELETE from films WHERE title= '"+ variable+"'")
        db.commit()
# del_film()