import sqlite3

db = sqlite3.connect("A.db")
cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS 'k' (x,y)")
cursor.execute("INSERT INTO 'k' VALUES ('5','6')")

###########################
#here:
cursor.execute("SELECT * FROM 'k'")
datas = cursor.fetchall()
###########################
for data in datas:
    print(data)
###########################
#What is cursor.fetchall()
print(cursor.fetchall())
#What is cursor.fetchmany()
print(cursor.fetchmany(5))

db.commit()
db.close()