"""
@author: Maneesh D
@date: 29-May-17
@intepreter: Python 3.6
"""
import sqlite3


def store_data():
    with sqlite3.connect("store.db") as con:
        cur = con.cursor()
        print("Fetching columns from from db Store....\n")
        for l in cur.execute("PRAGMA table_info('Store');").fetchall():
            print(l)
        col_names = [cn[1] for cn in cur.execute("PRAGMA table_info('Store');")]
        header = "%-17s %-19s %-30s %-2s" % (col_names[0], col_names[1], col_names[2], col_names[3])
        print("-" * (len(header) + 22))
        print(header)
        print("-" * (len(header)+22))

if __name__ == '__main__':
    store_data()
