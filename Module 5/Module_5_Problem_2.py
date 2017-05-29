"""
@author: Maneesh D
@date: 29-May-17
@intepreter: Python 3.6

Get last inserted row id.
"""
import sqlite3


con = sqlite3.connect("test.db")
tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='Friends';"
with con:
    cur = con.cursor()
    if not cur.execute(tb_exists).fetchone():
        cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
    cur.execute("DELETE FROM Friends;")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")
    print("The last Id of the inserted row is %d" % cur.lastrowid)
