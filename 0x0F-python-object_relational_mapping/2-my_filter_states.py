#!/usr/bin/python3
"""Displays values in a table where name matches argument"""
import MySQLdb
import sys

if __name__ == "__main__":
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    filter_value = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         passwd=MY_PASS,
                         user=MY_USER,
                         db=MY_DB)
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name = '{:s}' ORDER BY states.id"
    cur.execute(sql.format(filter_value))
    myresult = cur.fetchall()

    for x in myresult:
        print(x)

    cur.close()
    db.close()
