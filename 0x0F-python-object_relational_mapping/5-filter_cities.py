#!/usr/bin/python3
"""Takes in a `state` and lists `cities` by state.id"""
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
    sql = "WITH temporaryTable(id) as \
        (SELECT id \
        FROM states \
        WHERE name = %s) \
        SELECT name \
        FROM cities, temporaryTable \
        WHERE state_id = temporaryTable.id"
    cur.execute(sql, (filter_value, ))
    myresult = cur.fetchall()

    j = len(myresult)
    myList = []
    for x in myresult:
        myList.append(x[0])

    y = ", ".join(myList)
    print(y)

    cur.close()
    db.close()
