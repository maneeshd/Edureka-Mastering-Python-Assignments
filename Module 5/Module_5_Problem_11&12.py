"""
@author: Maneesh D
@date: 29-May-17
@intepreter: Python 3.6
"""
import csv
import sqlite3

csv_file = "sample-storedata.csv"


def store_data():
    table_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='Store';"
    with sqlite3.connect("store.db") as con, open(csv_file) as fr:
        cur = con.cursor()
        if not cur.execute(table_exists).fetchone():
            cur.execute("CREATE TABLE Store(Latitude REAL, Longitude REAL, Phone TEXT, Address TEXT);")

        # Get Store Data from csv file
        csv_data = csv.reader(fr)

        print("Adding CSV Store Data to Database...")
        # for data in csv_data:
        #     cur.execute("INSERT INTO Store(Latitude,Longitude,Phone,Address) VALUES(?,?,?,?)",
        #                 (data[0], data[1], data[2], data[3]))
        cur.executemany("INSERT INTO Store(Latitude,Longitude,Phone,Address) VALUES(?,?,?,?)", csv_data)
        cur.execute("commit;")

        print("Fetching added data from db to verify....\n")
        col_names = [cn[1] for cn in cur.execute("PRAGMA table_info('Store');")]
        cur.execute('SELECT * FROM Store;')
        rows = cur.fetchall()
        header = "%-17s %-19s %-30s %-2s" % (col_names[0], col_names[1], col_names[2], col_names[3])
        print("-" * (len(header) + 22))
        print(header)
        print("-" * (len(header)+22))
        for row in rows:
            print("%-16s %-16s %-18s %-32s" % row)

        cur.execute("DELETE FROM Store;")
        cur.execute("commit;")


if __name__ == '__main__':
    store_data()
