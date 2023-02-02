import sqlite3

# I dec. the dataset
dataset = [
    (5,6,7),
    (10,15,20),
    (8,20,66)
]

db= sqlite3.connect("total.db")
c = db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS databaseT (X,Y,Z)")
######################################################
#Here is the answer:
for data in dataset:
    c.execute("INSERT INTO 'databaseT' VALUES (?,?,?)",data)
#######################################################
# (?,?,?) = (5,6,7) #
db.commit()

db.close()