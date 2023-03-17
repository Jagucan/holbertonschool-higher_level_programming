#!/usr/bin/python3

"""
This script lists all states from the database hbtn_0e_0_usa
Arguments:
   username - MySQL username
   password - MySQL password
   database - Database name
"""

import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                                passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE UPPER(name) LIKE 'N%'")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
