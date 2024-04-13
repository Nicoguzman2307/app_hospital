import tkinter as tk
from tkinter import messagebox

# Base de datos simulada para almacenar usuarios registrados
usuarios_registrados = {
    "usuario1": "contraseña1",
    "usuario2": "contraseña2"
}

# Función para iniciar sesión
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Verificar si el usuario y la contraseña son válidos
    if username in usuarios_registrados and usuarios_registrados[username] == password:
        messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido, {username}!")
    else:
        messagebox.showerror("Error de inicio de sesión", "Usuario o contraseña incorrectos")

# Función para registrar un nuevo usuario
def register():
    new_username = entry_new_username.get()
    new_password = entry_new_password.get()

    if new_username == "" or new_password == "":
        messagebox.showerror("Error de registro", "Por favor, ingrese un usuario y una contraseña válidos")
    elif new_username in usuarios_registrados:
        messagebox.showerror("Error de registro", "El usuario ya existe. Por favor, elija otro nombre de usuario.")
    else:
        usuarios_registrados[new_username] = new_password
        messagebox.showinfo("Registro exitoso", "¡Registro completado! Ahora puede iniciar sesión.")

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Inicio de Sesión")

# Etiquetas y campos de entrada para inicio de sesión
label_username = tk.Label(root, text="Usuario:")
label_username.pack(pady=(10, 0))
entry_username = tk.Entry(root)
entry_username.pack(pady=(0, 10))

label_password = tk.Label(root, text="Contraseña:")
label_password.pack(pady=(10, 0))
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=(0, 20))

login_button = tk.Button(root, text="Iniciar sesión", command=login)
login_button.pack()

# Separador visual entre secciones
separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=5, pady=5)

# Etiquetas y campos de entrada para registro
label_new_username = tk.Label(root, text="Nuevo usuario:")
label_new_username.pack(pady=(10, 0))
entry_new_username = tk.Entry(root)
entry_new_username.pack(pady=(0, 10))

label_new_password = tk.Label(root, text="Nueva contraseña:")
label_new_password.pack(pady=(10, 0))
entry_new_password = tk.Entry(root, show="*")
entry_new_password.pack(pady=(0, 20))

register_button = tk.Button(root, text="Registrarse", command=register)
register_button.pack()

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()