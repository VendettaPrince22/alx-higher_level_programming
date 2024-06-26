#!/usr/bin/python3
"""Lists all `states` with name starting with N from database"""
import MySQLdb
import sys

if __name__ == "__main__":
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         passwd=MY_PASS,
                         user=MY_USER,
                         db=MY_DB)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name \
                LIKE BINARY 'N%' ORDER BY states.id")
    myresult = cur.fetchall()

    for x in myresult:
        print(x)

    cur.close()
    db.close()
