"""
@author: Maneesh D
@date: 29-May-17
@intepreter: Python 3.6
"""
import sqlite3 as lite


con = lite.connect('test.db')
tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='Cars';"
with con:
    cur = con.cursor()
    if not cur.execute(tb_exists).fetchone():
        cur.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name TEXT);")
        cur.execute("INSERT INTO Cars(Name) VALUES ('Audi R8');")
        cur.execute("INSERT INTO Cars(Name) VALUES ('Lexus LFA');")
        cur.execute("INSERT INTO Cars(Name) VALUES ('Lamborghini Aventador');")
        cur.execute("INSERT INTO Cars(Name) VALUES ('McLaren P1');")
    cur.execute("SELECT * FROM Cars;")
    for colinfo in cur.fetchall():
        print(colinfo)
