import sqlite3


conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT, telefono TEXT,email TEXT, ciudad TEXT, direccion TEXT)""")
conn.commit()

#Crear usuarios 
def create_user(name, telefono, email, ciudad, direccion):
    cursor.execute("INSERT INTO users (name, telefono, email, ciudad, direccion) VALUES (?, ?)", (name, telefono, email, ciudad, direccion))
    conn.commit()

def read_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#Actualizar todos los datos
def update_user(id, name, telefono, email, ciudad, direccion):
    cursor.execute("UPDATE users SET telefono = ?, email = ?, ciudad = ?, direccion = ? WHERE id = ?", (name, telefono, email, ciudad, direccion, id))
    conn.commit()

#Actualizar telefono
def update_user(id, telefono):
    cursor.execute("UPDATE users SET telefono = ? WHERE id = ?", (telefono, id))
    conn.commit()

#Actualizar email
def update_user(id, email):
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (email, id))
    conn.commit()

def delete_user(id):
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()


conn.close()