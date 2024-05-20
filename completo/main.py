import flet as ft
import sqlite3
import datetime

def init_db():
    conn = sqlite3.connect('database_hospital.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            apellidos TEXT,
            edad INTEGER,
            sexo TEXT,
            cedula TEXT UNIQUE,
            password TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            codigo TEXT UNIQUE,
            password TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            doctor_id INTEGER,
            date TEXT,
            time TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(doctor_id) REFERENCES doctors(id)
        )
    ''')
    conn.commit()
    conn.close()

def main(page: ft.Page):
    page.title = "Hospital - Registro e Inicio de Sesión"
    
    def show_register(e):
        page.controls.clear()
        page.add(register_layout)
        page.update()

    def show_login(e):
        page.controls.clear()
        page.add(login_layout)
        page.update()
    
    # Función para cerrar el diálogo
    def close_dialog(e):
        page.dialog.open = False
        page.update()
    
    # Función para mostrar mensajes de alerta
    def show_alert(title, message):
        alert_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(title),
            content=ft.Text(message),
            actions=[
                ft.TextButton("OK", on_click=close_dialog)
            ]
        )
        page.dialog = alert_dialog
        alert_dialog.open = True
        page.update()
    
    # Función para registrar un nuevo usuario
    def register_user(e):
        if not all([nombre.value, apellidos.value, edad.value, sexo.value, cedula.value, password.value, confirm_password.value]):
            show_alert("Error", "Todos los campos son obligatorios")
            return

        if password.value != confirm_password.value:
            show_alert("Error", "Las contraseñas no coinciden")
            return
        
        conn = sqlite3.connect('database_hospital.db')
        c = conn.cursor()
        try:
            c.execute('''
                INSERT INTO users (nombre, apellidos, edad, sexo, cedula, password) VALUES (?, ?, ?, ?, ?, ?)
            ''', (nombre.value, apellidos.value, int(edad.value), sexo.value, cedula.value, password.value))
            conn.commit()
            show_alert("Éxito", "Registro exitoso")
        except sqlite3.IntegrityError:
            show_alert("Error", "La cédula ya está registrada")
        conn.close()
    
    # Función para iniciar sesión
    def login_user(e):
        if not all([login_cedula.value, login_password.value]):
            show_alert("Error", "Cédula y contraseña son obligatorios")
            return
        
        conn = sqlite3.connect('database_hospital.db')
        c = conn.cursor()
        c.execute('''
            SELECT * FROM users WHERE cedula = ? AND password = ?
        ''', (login_cedula.value, login_password.value))
        user = c.fetchone()
        conn.close()
        
        if user:
            dashboard_page(user)
        else:
            show_alert("Error", "Cédula o contraseña incorrecta")

    # Página del panel de control después del inicio de sesión
    def dashboard_page(user):
        page.controls.clear()
        page.add(ft.Text(f"Bienvenido, {user[1]} {user[2]}", size=20))
        page.add(ft.ElevatedButton(text="Conocer sobre el hospital", on_click=lambda e: show_about(user)))
        page.add(ft.ElevatedButton(text="Agendar citas", on_click=lambda e: show_appointments(user)))
        page.update()
    
    # Página para "Conocer sobre el hospital"
    def show_about(user):
        page.controls.clear()
        page.add(ft.Text("Conocer sobre el hospital", size=20))
        page.add(ft.Text("¡Información sobre el hospital aquí!"))
        page.add(ft.ElevatedButton(text="Volver al panel de control", on_click=lambda e: dashboard_page(user)))
        page.update()
    
    # Página para "Agendar citas"
    def show_appointments(user):
        page.controls.clear()

        def change_date(e):
            print(f"Date picker changed, value is {date_picker.value}")

        def date_picker_dismissed(e):
            print(f"Date picker dismissed, value is {date_picker.value}")

        date_picker = ft.DatePicker(
            on_change=change_date,
            on_dismiss=date_picker_dismissed,
            first_date=datetime.datetime(2023, 10, 1),
            last_date=datetime.datetime(2024, 10, 1),
        )

        page.overlay.append(date_picker)

        date_button = ft.ElevatedButton(
            "Pick date",
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: date_picker.pick_date(),
        )

        time_picker = ft.Dropdown(
            label="Seleccione una hora",
            options=[
                ft.dropdown.Option("08:00"), ft.dropdown.Option("09:00"), ft.dropdown.Option("10:00"),
                ft.dropdown.Option("11:00"), ft.dropdown.Option("12:00"), ft.dropdown.Option("13:00"),
                ft.dropdown.Option("14:00"), ft.dropdown.Option("15:00"), ft.dropdown.Option("16:00"),
                ft.dropdown.Option("17:00")
            ]
        )
        doctor_id = ft.TextField(label="ID del Doctor")

        def schedule_appointment(e):
            if not (date_picker.value and time_picker.value and doctor_id.value):
                show_alert("Error", "Todos los campos son obligatorios")
                return

            conn = sqlite3.connect('database_hospital.db')
            c = conn.cursor()
            c.execute('''
                INSERT INTO appointments (user_id, doctor_id, date, time) VALUES (?, ?, ?, ?)
            ''', (user[0], int(doctor_id.value), date_picker.value, time_picker.value))
            conn.commit()
            conn.close()
            show_alert("Éxito", "Cita agendada exitosamente")
        
        page.add(ft.Text("Agendar citas", size=20))
        page.add(date_button)
        page.add(time_picker)
        page.add(doctor_id)
        page.add(ft.ElevatedButton(text="Agendar", on_click=schedule_appointment))
        page.add(ft.ElevatedButton(text="Volver al panel de control", on_click=lambda e: dashboard_page(user)))
        page.update()
    
    # Función para iniciar sesión como médico
    def login_doctor(e):
        code = doctor_code.value
        password = doctor_password.value
        
        conn = sqlite3.connect('database_hospital.db')
        c = conn.cursor()
        c.execute('''
            SELECT * FROM doctors WHERE codigo = ? AND password = ?
        ''', (code, password))
        doctor = c.fetchone()
        conn.close()
        
        if doctor:
            doctor_dashboard(doctor)
        else:
            show_alert("Error", "Código o contraseña incorrectos")

    # Página del panel de control después de iniciar sesión como médico
    def doctor_dashboard(doctor):
        page.controls.clear()
        page.add(ft.Text(f"Bienvenido, {doctor[1]}", size=20))
        page.add(ft.ElevatedButton(text="Revisar mis citas", on_click=lambda e: show_doctor_appointments(doctor)))
        page.add(ft.ElevatedButton(text="Volver al inicio de sesión de médicos", on_click=lambda e: show_doctor_login()))
        page.update()
    
    # Página para "Revisar mis citas" como médico
    def show_doctor_appointments(doctor):
        page.controls.clear()
        page.add(ft.Text("Mis Citas", size=20))
        
        conn = sqlite3.connect('database_hospital.db')
        c = conn.cursor()
        c.execute('''
            SELECT users.nombre, users.apellidos, appointments.date, appointments.time
            FROM appointments
            INNER JOIN users ON appointments.user_id = users.id
            WHERE doctor_id = ?
        ''', (doctor[0],))
        appointments = c.fetchall()
        conn.close()
        
        if appointments:
            for appointment in appointments:
                page.add(ft.Text(f"Paciente: {appointment[0]} {appointment[1]}, Fecha: {appointment[2]}, Hora: {appointment[3]}"))
        else:
            page.add(ft.Text("No tienes citas programadas"))
        
        page.add(ft.ElevatedButton(text="Volver al panel de control", on_click=lambda e: doctor_dashboard(doctor)))
        page.update()
    
    # Elementos de la interfaz de registro
    nombre = ft.TextField(label="Nombre")
    apellidos = ft.TextField(label="Apellidos")
    edad = ft.TextField(label="Edad", keyboard_type=ft.KeyboardType.NUMBER)
    sexo = ft.Dropdown(label="Sexo", options=[
        ft.dropdown.Option("Masculino"),
        ft.dropdown.Option("Femenino")
    ])
    cedula = ft.TextField(label="Cédula")
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    confirm_password = ft.TextField(label="Confirmar Contraseña", password=True, can_reveal_password=True)
    register_button = ft.ElevatedButton(text="Registrar", on_click=register_user)

    # Layout de registro
    register_layout = ft.Column([
        ft.Text("Registro", size=20),
        nombre,
        apellidos,
        edad,
        sexo,
        cedula,
        password,
        confirm_password,
        register_button,
        ft.ElevatedButton(text="Volver", on_click=lambda e: show_initial_buttons())
    ], spacing=10)
    
    # Elementos de la interfaz de inicio de sesión
    login_cedula = ft.TextField(label="Cédula")
    login_password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    login_button = ft.ElevatedButton(text="Iniciar Sesión", on_click=login_user)

    # Layout de inicio de sesión
    login_layout = ft.Column([
        ft.Text("Inicio de Sesión", size=20),
        login_cedula,
        login_password,
        login_button,
        ft.ElevatedButton(text="Volver", on_click=lambda e: show_initial_buttons())
    ], spacing=10)
    
    # Elementos de la interfaz de inicio de sesión para médicos
    doctor_code = ft.TextField(label="Código")
    doctor_password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    doctor_login_button = ft.ElevatedButton(text="Iniciar Sesión como Médico", on_click=login_doctor)

    # Layout de inicio de sesión para médicos
    doctor_login_layout = ft.Column([
        ft.Text("Inicio de Sesión para Médicos", size=20),
        doctor_code,
        doctor_password,
        doctor_login_button,
        ft.ElevatedButton(text="Volver", on_click=lambda e: show_initial_buttons())
    ], spacing=10)
    
    # Función para mostrar el inicio de sesión de médicos
    def show_doctor_login():
        page.controls.clear()
        page.add(doctor_login_layout)
        page.update()
    
    # Botones iniciales
    def show_initial_buttons():
        page.controls.clear()
        initial_buttons_layout = ft.Column([
            ft.ElevatedButton(text="Iniciar Sesión", on_click=show_login),
            ft.ElevatedButton(text="Registro", on_click=show_register),
            ft.ElevatedButton(text="Iniciar Sesión como Médico", on_click=lambda e: show_doctor_login())
        ], spacing=10, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        page.add(
            ft.Row(
                [initial_buttons_layout], 
                alignment=ft.MainAxisAlignment.CENTER, 
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )
        )
        page.update()
    
    show_initial_buttons()

# Inicializar la base de datos y ejecutar la aplicación
init_db()
ft.app(target=main)