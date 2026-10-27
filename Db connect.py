import sqlite3

conn = sqlite3.coonect("sport.db")
conn.execute("PRAGMA foreign_keys = ON")
