import sqlite3
import hashlib


conexion = sqlite3.connect("usuarios.db")

cursor = conexion.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    password TEXT
)
""")


usuarios = [
    ("Alejandro", "1234"),
    ("Sebastian", "5678"),
    ("Gonzalez", "abcd")
]


for usuario, clave in usuarios:

    password_hash = hashlib.sha256(
        clave.encode()
    ).hexdigest()


    cursor.execute(
        "INSERT INTO usuarios(nombre,password) VALUES (?,?)",
        (usuario,password_hash)
    )


conexion.commit()

conexion.close()


print("Usuarios creados correctamente")
