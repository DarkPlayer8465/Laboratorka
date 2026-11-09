import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "sports.db"
SCHEMA_PATH = Path(__file__).parent / "schema.sql"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    # PRAGMA действует только для текущего подключения,
    # поэтому включаем его при каждом подключении, а не только в schema.sql
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    conn = get_connection()
    with open(SCHEMA_PATH, encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()