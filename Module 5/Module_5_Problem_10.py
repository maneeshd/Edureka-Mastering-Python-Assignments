"""
@author: Maneesh D
@date: 29-May-17
@intepreter: Python 3.6
"""
import sqlite3 as lite


con = lite.connect('todo.db')
with con:
    cur = con.cursor()

    col_names = [cn[1] for cn in cur.execute("PRAGMA table_info('Cars');")]
    cur.execute('SELECT * FROM Cars;')
    rows = cur.fetchall()

    print("%s %-10s %s" % (col_names[0], col_names[1], col_names[2]))
    for row in rows:
        print("%2s %-10s %s" % row)
