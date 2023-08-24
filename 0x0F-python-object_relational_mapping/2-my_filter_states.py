#!/usr/bin/python3
""" Takes an arg and displays al values matching it """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], arg=sys.argv[4]
                         port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'"
    cur.execute(query).format(sys.argv[4]))

    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    db.close()
