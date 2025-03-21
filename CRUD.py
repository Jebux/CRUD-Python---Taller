import sqlite3


conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, telefono TEXT, email TEXT, ciudad TEXT, direccion TEXT)")
conn.commit()

#Crear usuarios 
def create_user(name, telefono, email, ciudad, direccion):
    cursor.execute("INSERT INTO users (name, telefono, email, ciudad, direccion) VALUES (?, ?, ?,? ,?)", (name, telefono, email, ciudad, direccion))
    conn.commit()

def read_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#Actualizar todos los datos
def update_user_data(id, telefono, email, ciudad, direccion):
    cursor.execute("UPDATE users SET telefono = ?, email = ?, ciudad = ?, direccion = ? WHERE id = ?", ( telefono, email, ciudad, direccion, id))
    conn.commit()

#Actualizar telefono
def update_user_telefono(id, telefono):
    cursor.execute("UPDATE users SET telefono = ? WHERE id = ?", (telefono, id))
    conn.commit()

#Actualizar email
def update_user_email(id, email):
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (email, id))
    conn.commit()

def delete_user(id):
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()

"""
# Ejemplo de uso
#create_user("Alice", "alice@mail.com")  # Crear un usuario
#create_user("Wanda", "wanda@mail.com")
#create_user("lola", "lola@mail.com")
print(read_users())  # Ver todos los usuarios
update_user(2, "Alice Updated", "alice_updated@mail.com")  # Actualizar usuario
delete_user(4)  # Eliminar usuario
print(read_users())

"""

#name, telefono, email, ciudad, direccion

"""
create_user("Alice", "3205867946","alice@mail.com", "Giron", "Carrera 25 N 35 - 16" )  
create_user("Wanda", "3215467984", "wanda@mail.com", "Bucaramanga", "Calle 35 N 50 - 33")
create_user("Jesus", "3115458967","jesus@mail.com", "Giron", "Carrera 14 N 23 - 42")
create_user("Juan", "3013256974","juan@mail.com", "Floridablanca", "Calle 105 N 32 - 14")
create_user("Tatiana","3056594812", "tatiana@mail.com", "Giron", "Avenida 12 N 23 - 94")
create_user("Jennifer","3156497832", "jennifer@mail.com", "Bucaramanga", "Diagonal 15 N 15-43")
"""


usuarios = read_users()

for user in usuarios:
    print(user)

print("""
      
Inicio de programa
      
¿Qué desea realizar?
      
1. Modificar telefono de un usuario definido
2. Modificar email de un usuario defindo
3. Modificar todos los datos del usuario
       
""")

accion = input("Ingrese la opción que desea realizar: ")

opciones = ["1","2","3"]

while accion not in opciones:
    accion = input("Opcion incorrecta ingrese nuevamente la opción que desea realizar")

if accion == "1":
    id_usuario = input("Ingrese el id de usuario a modificar el telefono: ")
    telefono_usuario = input("Ingrese el nuevo el telefono: ")
    update_user_telefono(id_usuario,telefono_usuario)

if accion == "2":
    id_usuario = input("Ingrese el id de usuario a modificar el telefono: ")
    email_usuario = input("Ingrese el nuevo el email: ")
    update_user_email(id_usuario,email_usuario)

if accion == "3":
    id_usuario = input("Ingrese el id del usuario: ")
    telefono_usuario = input("Ingrese el nuevo el telefono: ")
    email_usuario = input("Ingrese el nuevo email: ")
    ciudad_usuario = input("Ingrese la nueva ciudad: ")
    direccion_usuario = input("Ingrese la nueva dirección: ")
    update_user_data(id_usuario,telefono_usuario, email_usuario, ciudad_usuario, direccion_usuario) 
    

conn.close()