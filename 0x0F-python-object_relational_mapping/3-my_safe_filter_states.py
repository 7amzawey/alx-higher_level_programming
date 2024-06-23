#!/usr/bin/python3
""" This script return all states """
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
            "GRANT SELECT, INSERT, UPDATE, CREATE, DROP, ALTER ON 
            db.states TO user@localhost;
            FLUSH PRIVILEGES;
            SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id".
            format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
