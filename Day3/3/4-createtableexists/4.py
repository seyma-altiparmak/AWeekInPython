#IF EXISTS F.
import sqlite3

db = sqlite3.connect("exits.db")

cursor = db.cursor()
cursor.execute("CREATE TABLE myTable (d,n,m)")
cursor.execute("CREATE TABLE IF NOT EXISTS 'me' (name)")

db.close()