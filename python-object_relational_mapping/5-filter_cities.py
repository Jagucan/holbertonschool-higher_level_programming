#!/usr/bin/python3

"""
This script takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                                passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities\
                LEFT JOIN states ON states.id = cities.state_id\
                WHERE states.name = %s ORDER BY cities.id ASC", (state,))
    query_rows = cur.fetchall()
    cities = [row[0] for row in query_rows]
    print(", ".join(cities))
    cur.close()
    conn.close()
