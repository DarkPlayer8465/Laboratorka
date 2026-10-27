import sqlite3

conn = sqlite3.connect("sport.db")
conn.execute("PRAGMA foreign_keys = ON")
