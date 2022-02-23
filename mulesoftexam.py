
# import the sqlite3 package
import sqlite3

# create a database named backup
cnt = sqlite3.connect("ms_movies.db")

# create a table named gfg
cnt.execute('''CREATE TABLE movie(
NO.
ACTOR TEXT,
ACTRESS TEXT,
Y.O.R. INT
DIRECTOR TEXT);''')

# to insert data into the database


cnt.execute('''INSERT INTO movie VALUES(
1, 'Shahrukh khan','Kajol', 2007, 'Karan Johar');''')

# insert in different order
cnt.execute('''INSERT INTO gfg(ACCURACY, POINTS, NAME) VALUES(
2, 'Salman khan','Kajol', 2009, 'Karan Johar');''')

cnt.execute('''INSERT INTO gfg(NAME, ACCURACY, POINTS) VALUES(
3, 'Shahrukh khan','Juhi Chawla', 20011, 'Abbas Mastan');''')

# commit changes to the database
cnt.commit()

# to retrieve data

cnt.execute('''(SELECT * FROM movie)''';)
