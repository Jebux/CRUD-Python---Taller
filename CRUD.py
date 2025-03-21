import sqlite3


conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT, teléfono TEXT,email TEXT, ciudad TEXT, direccion TEXT)""")
conn.commit()

