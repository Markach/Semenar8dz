
import sqlite3

db = sqlite3.connect("details.db")
cursor=db.cursor()

# cursor.execute(""" CREATE TABLE IF NOT EXISTS films(id integer PRIMARY KEY AUTOINCREMENT, title text NOT NULL, genre text, country text, 
# release_year integer, audience_rating real, language text);""")

# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("Матрица", "боевик","США", 1999, 8.8, "английский"))
# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("Война будущего", "боевик","США", 2021, 6.3, "английский"))
# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("Серый человек", "боевик","США", 2022, 8.6, "английский"))
# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("Полтора шпиона", "боевик","США", 2016, 6.3, "английский"))
# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("Джуманджи: Новый уровень", "боевик","США", 2019, 6.6, "английский"))
# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("Титаник", "драма","США", 1997, 9.2, "английский"))
# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("Легенды осени", "драма","США", 1994, 8.6, "английский"))
# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("Загадочная история Бенджамина Баттона", "драма","США", 2008, 9.5, "английский"))
# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("Звёздочки на земле", "драма","Индия", 2007, 8.8, "английский"))
# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("Дневник памяти", "драма","США", 2004, 9.1, "английский"))
# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("Выпускной класс", "комедия","США", 2022, 6.8, "английский"))
# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("Первый встречный", "комедия","США", 2022, 6.7, "английский"))
# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("Джентльмены удачи", "комедия","СССР", 1971, 8.7, "русский"))
# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("Служебный роман", "комедия","СССР", 1977, 8.8, "русский"))
# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("12 стульев", "комедия","СССР", 1971, 8.4, "русский"))
# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("Мумия", "ужасы","США", 2017, 7.4, "английский"))
# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("Звонок", "ужасы","США", 2002, 9.3, "английский"))
# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("Оно", "ужасы","Канада", 2017, 8.0, "английский"))
# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("Мгла", "ужасы","США", 2007, 9.1, "английский"))
# cursor.execute("INSERT INTO films(title, genre, country, release_year, audience_rating, language) VALUES(?,?,?,?,?,?)", ("Проклятие", "ужасы","Япония", 2002, 7.4, "английский"))


# db.commit()