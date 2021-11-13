import sqlite3
from sqlite3 import Error




def create_connection(dbfile):
    conn=None
    try:
        conn=sqlite3.connect(dbfile)
    except Error as e:
        print(e)

    return conn

if __name__ == "__main__":
    create_connection("pythonsqlite.db")

    

