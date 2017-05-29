"""
@author: Maneesh D
@date: 29-May-17
@intepreter: Python 3.6

Getting the Sqlite3 Database Version
"""
import sqlite3


con = sqlite3.connect("test.db")
with con:
    cur = con.cursor()
    cur.execute("SELECT sqlite_version();")

    data = cur.fetchone()

    print("SQLite version: %s" % data)
