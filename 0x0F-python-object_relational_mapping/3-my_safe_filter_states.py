#!/usr/bin/python3
""" This script returns all states matching a name safely from SQL injections """
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    # Use parameterized query to prevent SQL injection
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id", (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
