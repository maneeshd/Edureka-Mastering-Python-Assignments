"""
@author: Maneesh D
@date: 29-May-17
@intepreter: Python 3.6
"""
import sqlite3 as lite


con = lite.connect('todo.db')
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars;")
    rows = cur.fetchall()
    for row in rows:
        print(row)