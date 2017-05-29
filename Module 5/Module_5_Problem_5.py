"""
@author: Maneesh D
@date: 29-May-17
@intepreter: Python 3.6


"""
import sqlite3 as lite


cars = [
        [1, 'Audi', 52642],
        [2, 'Mercedes', 57127],
        [3, 'Skoda', 9000],
        [4, 'Volvo', 29000],
        [5, 'Bentley', 350000],
        [6, 'Hummer', 41400],
        [7, 'Volkswagen', 21600]
        ]

con = lite.connect('todo.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars;")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT);")
    cur.executemany("INSERT INTO Cars VALUES(?, ?, ?);", cars)
    cur.execute("SELECT * FROM Cars;")
    for row in cur.fetchall():
        print(row)
