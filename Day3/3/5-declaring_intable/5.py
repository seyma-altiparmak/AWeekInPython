import sqlite3

db = sqlite3.connect("databa.db")

cursor = db.cursor()
cursor.execute("CREATE TABLE sums (X,Y)")
#Declaring
cursor.execute("INSERT INTO 'sums' VALUES ('5','6')")
#assign in table
db.commit()

db.close()