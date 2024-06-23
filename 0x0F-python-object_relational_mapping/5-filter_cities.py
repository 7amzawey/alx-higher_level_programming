#!/usr/bin/python3
""" This script returns all
states matching a name safely from SQL injections """
if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute(
            """SELECT GROUP_CONCAT(c.name SEPARATOR ', ')
            FROM cities AS c
            JOIN states AS s ON s.id = c.state_id
            WHERE s.name LIKE BINARY %s
            ORDER BY c.id""", [argv[4]]
            )
    row = cur.fetchone()
    if row and row[0]:
        print(row[0])
    cur.close()
    db.close()
