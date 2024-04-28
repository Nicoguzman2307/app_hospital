import flet as ft
import sqlite3

# Conexión a la base de datos SQLite
connection = sqlite3.connect('usuarios.db')
cursor = connection.cursor()

# Crear la tabla de usuarios si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        username TEXT PRIMARY KEY,
        password TEXT
    )
''')
connection.commit()

# Función para registrar un nuevo usuario en la base de datos
def registrar_usuario(username, password):
    try:
        cursor.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', (username, password))
        connection.commit()
        return True
    except sqlite3.IntegrityError:
        return False

# Función para iniciar sesión
def iniciar_sesion(username, password):
    cursor.execute('SELECT * FROM usuarios WHERE username=? AND password=?', (username, password))
    if cursor.fetchone() is not None:
        return True
    else:
        return False

# Función principal para la aplicación Flet
def main(page):
    page.add(ft.SafeArea(
        ft.Column(
            [
                ft.Text("Registro e Inicio de Sesión"),
                ft.Text("Username:"),
                ft.TextField(key="username"),
                ft.Text("Password:"),
                ft.TextField(key="password"),  # Corregido a obscure
                ft.ElevatedButton("Registrarse", on_click=registrar),
                ft.ElevatedButton("Iniciar Sesión", on_click=iniciar),
                ft.Text(id="mensaje", style=ft.TextStyle),
            ]
        )
    ))

# Función para manejar el evento de registro
def registrar(event):
    username = event.page.get("username")
    password = event.page.get("password")
    if username and password:
        if registrar_usuario(username, password):
            event.page.set("mensaje", "Registro exitoso")
        else:
            event.page.set("mensaje", "El usuario ya existe")

# Función para manejar el evento de inicio de sesión
def iniciar(event):
    username = event.page.get("username")
    password = event.page.get("password")
    if username and password:
        if iniciar_sesion(username, password):
            event.page.set("mensaje", "Inicio de sesión exitoso")
        else:
            event.page.set("mensaje", "Usuario o contraseña incorrectos")

# Ejecutar la aplicación Flet
ft.app(target=main)
