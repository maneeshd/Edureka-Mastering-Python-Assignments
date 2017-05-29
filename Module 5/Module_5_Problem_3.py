"""
@author: Maneesh D
@date: 29-May-17
@intepreter: Python 3.6

Check if db file exists or not.
"""
import os
import sqlite3


db_filename = "todo.db"
db_is_new = not os.path.isfile(db_filename)
conn = sqlite3.connect(db_filename)
if db_is_new:
    print("Need to create schema")
    print("Creating database")
else:
    print("Database exists, assume schema does, too.")
conn.close()
