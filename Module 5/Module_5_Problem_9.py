"""
@author: Maneesh D
@date: 29-May-17
@intepreter: Python 3.6
"""
import sqlite3 as lite

con = lite.connect('todo.db')
with con:
    cur = con.cursor()
    cur.execute("PRAGMA table_info(Cars);")
    data = cur.fetchall()
    for d in data:
        print(d[0], d[1], d[2])
