-- List databases

import mysql.connector

cnx = mysql.connector.connect(user='root', password='root')

cursor = cnx.cursor()

query = "SELECT schema_name FROM information_schema.schemata"
cursor.execute(query)

databases = cursor.fetchall()
for db in databases:
    print(db[0])

cursor.close()
cnx.close()
