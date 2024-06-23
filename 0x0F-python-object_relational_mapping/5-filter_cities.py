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
            """SELECT c.name
            FROM states AS s
            JOIN cities AS c ON s.id = c.state_id
            WHERE s.name = '{}' 
            ORDER BY c.id""".format(argv(4))
            )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
