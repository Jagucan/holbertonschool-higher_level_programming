-- List databases

import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='localhost', database='information_schema')

cursor = cnx.cursor()

cursor.execute("SELECT schema_name FROM information_schema.schemata")

list_databases = cursor.fetchall()
print("List of databases:")
for row in list_databases:
    print(row[0])

cursor.close()
cnx.close()
