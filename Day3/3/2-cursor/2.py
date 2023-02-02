import sqlite3

db = sqlite3.connect("forcursor.db")

#CURSOR
cursor = db.cursor()

db.close