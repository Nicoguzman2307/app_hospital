import tkinter as tk
from tkinter import messagebox
import sqlite3

# se conecta a la base de datos
Coneccion_Base_Datos = sqlite3.connect('usuarios.db')
cursor = Coneccion_Base_Datos.cursor()

# esto crea la base de datos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        username TEXT PRIMARY KEY,
        password TEXT,
        tipo_de_documento TEXT,
        numerodoc TEXT,
        correo TEXT,
        sexo TEXT
    )
''')
Coneccion_Base_Datos.commit()

# Función para iniciar sesión
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Verificar la base de datos
    cursor.execute('SELECT * FROM usuarios WHERE username=? AND password=?', (username, password))
    if cursor.fetchone() is not None:
        messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido, {username}!")
    else:
        messagebox.showerror("Error de inicio de sesión", "Usuario o contraseña incorrectos")

# Función para registrar un nuevo usuario
def register():
    new_username = entry_new_username.get()
    new_password = entry_new_password.get()
    new_tipo_doc = selected_tipo_doc.get()
    new_num_documento = entry_new_documento.get()
    new_correo = entry_new_correo.get()
    new_sexo = entry_new_sexo.get()

    if new_username == "" or new_password == "" or new_tipo_doc == "" or new_num_documento == "" or new_correo == "" or new_sexo == "":
        messagebox.showerror("Error de registro", "Por favor, llene todos los campos")
    else:
        try:
            # Insertar nuevo usuario en la base de datos
            cursor.execute('INSERT INTO usuarios (username, password, tipo_de_documento, numerodoc, correo, sexo) VALUES (?, ?, ?, ? , ?, ?)', 
                        (new_username, new_password, new_tipo_doc, new_num_documento, new_correo, new_sexo))
            Coneccion_Base_Datos.commit()
            messagebox.showinfo("Registro exitoso", "¡Registro completado! Ahora puede iniciar sesión.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error de registro", "El usuario ya existe. Por favor, elija otro nombre de usuario.")

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Inicio de Sesión")
#Agregamos una imagen como icono e imagen a la pantalla - David
root.iconbitmap("Actualizacion log in/inicio de sesion/Cruz.ico")

image_frame = tk.Frame(root)
image_frame.pack(pady=(20,0))

image = tk.PhotoImage(file="Actualizacion log in/inicio de sesion/Cruz.gif")
image = image.subsample(2,2)
label= tk.Label(image_frame, image=image)
label.pack()
#Mensaje para indicar el inicio de sesión - David
label_mensaje_inicio_sesion = tk.Label(root, text= "En caso de tener usuario, inicie sesión aquí", font=("Arial", 13,"bold"))
label_mensaje_inicio_sesion.pack()

#ajustamos el tamaño
root.geometry("600x800")

# Etiquetas para el inicio de sesión
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
#Mensaje registro - David
label_salto_registro = tk.Label(root,text = "")
label_salto_registro.place(relx=0.5, rely=5.0, anchor="center")
label_mensaje_registro = tk.Label(root, text = "En caso de no tener usuario, registrese aquí", font=("Arial", 13, "bold"))
label_mensaje_registro.pack()

# Etiquetas y campos de entrada para registro
label_new_username = tk.Label(root, text="Nuevo usuario:")
label_new_username.pack(pady=(10, 0))
entry_new_username = tk.Entry(root)
entry_new_username.pack(pady=(0, 10))

label_new_password = tk.Label(root, text="Nueva contraseña:")
label_new_password.pack(pady=(10, 0))
entry_new_password = tk.Entry(root, show="*")
entry_new_password.pack(pady=(0, 10))

# Etiquetas extras para el registro - David
label_new_tipo_doc = tk.Label(root, text="Seleccione su tipo de documento:")
label_new_tipo_doc.pack(pady=(10, 0))
#Menu tipo de documento - David
tipo_doc_opciones = ['Cédula de Ciudadanía', 'Tarjeta de Identidad', 'Cédula de Extranjería ']
selected_tipo_doc = tk.StringVar(root)
selected_tipo_doc.set(tipo_doc_opciones[0])
tipo_doc_menu = tk.OptionMenu(root, selected_tipo_doc, *tipo_doc_opciones)
tipo_doc_menu.pack(pady=(0,10))

label_new_documento = tk.Label(root, text="Ingrese su número de documento:")
label_new_documento.pack(pady=(10, 0))
entry_new_documento = tk.Entry(root)
entry_new_documento.pack(pady=(0,10))

label_new_correo = tk.Label(root, text="Ingrese su correo electrónico:")
label_new_correo.pack(pady=(10,0))
entry_new_correo = tk.Entry(root)
entry_new_correo.pack(pady=(0,10))

label_new_sexo = tk.Label(root, text="Ingrese su sexo:")
label_new_sexo.pack(pady=(10,0))
entry_new_sexo = tk.Entry(root)
entry_new_sexo.pack(pady=(0,10))

register_button = tk.Button(root, text="Registrarse", command=register)
register_button.pack()

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()

# Cerrar la conexión a la base de datos al salir
Coneccion_Base_Datos.close()
