#!/usr/bin/env python3
import MySQLdb
import sys

def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
