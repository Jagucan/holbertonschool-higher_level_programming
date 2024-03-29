#!/usr/bin/python3

"""
This script lists all cities
from the database hbtn_0e_4_usa
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
    cur.execute("SELECT cities.id, cities.name, states.name AS name\
                FROM cities LEFT JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
