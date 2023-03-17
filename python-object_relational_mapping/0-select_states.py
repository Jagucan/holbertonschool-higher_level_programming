#!/usr/bin/python3

"""
This script lists all states from the database hbtn_0e_0_usa
Arguments:
   username - MySQL username
   password - MySQL password
   database - Database name
Use: ./0-select_states.py 
"""

# This script lists all states from the database hbtn_0e_0_usa
# Arguments:
#    username - MySQL username
#    password - MySQL password
#    database - Database name
# Use: ./0-select_states.py 

import sys
import MySQLdb
    # import modules
    """ import modules """


if __name__ == "__main__":
    # get arguments
    """ get arguments """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="hbtn_0e_usa", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
