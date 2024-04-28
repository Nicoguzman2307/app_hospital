import flet as ft
import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Creación de la tabla de usuarios
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        username TEXT PRIMARY KEY,
        password TEXT
    )
''')
conn.commit()

def main(page: ft.Page):
    page.title = "Registro e Inicio de Sesión"

    # Campos de texto para usuario y contraseña
    username_input = ft.Text(value="Usuario")
    password_input = ft.Text(value="Contraseña")

    # Botones para registro e inicio de sesión
    register_button = ft.ElevatedButton(text="Registrarse")
    login_button = ft.ElevatedButton(text="Iniciar Sesión")

    # Lógica para registrar un nuevo usuario
    def register_user():
        username = username_input.value
        password = password_input.value
        cursor.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        print(f"Usuario {username} registrado correctamente.")

    # Lógica para verificar credenciales de inicio de sesión
    def login_user():
        username = username_input.value
        password = password_input.value
        cursor.execute('SELECT * FROM usuarios WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        if user:
            print(f"Bienvenido, {username}!")
        else:
            print("Credenciales incorrectas. Inténtalo de nuevo.")

    # Asignar funciones a los botones
    register_button.on_click(register_user)
    login_button.on_click(login_user)

    # Agregar los controles a la página
    page.add(
        username_input,
        password_input,
        register_button,
        login_button
    )

ft.app(target=main)
