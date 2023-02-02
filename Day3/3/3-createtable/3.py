#table
import sqlite3

db = sqlite3.connect("tables.db")

cursor = db.cursor()
#table:
cursor.execute("CREATE TABLE me (age,name,surname)")

#to check ==> sqlite-browser (https://sqlitebrowser.org/blog/version-3-12-2-released/)

db.close()