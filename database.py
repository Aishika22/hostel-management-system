import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    room INTEGER,
    fee INTEGER,
    status TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS admin(
    username TEXT,
    password TEXT
)
""")

# Insert hashed admin only once
cur.execute("SELECT * FROM admin WHERE username='admin'")
if not cur.fetchone():
    hashed_pw = generate_password_hash("admin123")
    cur.execute("INSERT INTO admin VALUES (?, ?)", ("admin", hashed_pw))

conn.commit()
conn.close()