"""
@author: Maneesh D
@date: 29-May-17
@intepreter: Python 3.6
"""
import sqlite3 as lite


con = lite.connect('todo.db')
with con:
    con.row_factory = lite.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")
    rows = cur.fetchall()
    for row in rows:
        print("%s %s %s" % (row["Id"], row["Name"], row["Price"]))
