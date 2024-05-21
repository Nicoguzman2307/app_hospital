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
    scroll=ft.ScrollMode.ALWAYS,
    page.fonts = {
        "Freeman-Regular": "Fonts/Freeman-Regular.ttf"
    }

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
        if len(password.value) < 8:
            show_alert("Error", "Se necesitan 8 o más caracteres para la contraseña")
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
        page.title = "Página principal del hospital"
        page.appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.LOCAL_HOSPITAL_ROUNDED),
            leading_width=50,
            title=ft.Text(
                "Hospital Fontibón E.S.E",
                color=ft.colors.BLACK,
                style=ft.TextStyle(font_family="Times New Roman"),
                weight=ft.FontWeight.BOLD
            ),
            center_title=True,
            bgcolor=ft.colors.BLUE,
            actions=[
                ft.Container(
                    content=ft.MenuBar(
                        style=ft.MenuStyle(
                            alignment=ft.alignment.top_left,
                            bgcolor=ft.colors.BLUE_200
                        ),
                        expand=True,
                        controls=[
                        ft.SubmenuButton(
                            content=ft.Text("Conoce más sobre el hospital aquí", color = ft.colors.BLACK, size = 18,
                                style= ft.TextStyle(font_family="Times New Roman"), weight=ft.FontWeight.BOLD),
                            controls=[
                                ft.MenuItemButton(
                                    content=ft.Text("Conoce nuestro equipo"),
                                leading=ft.Icon(ft.icons.PERSON),
                                on_click=lambda e: show_about(user)  # Pasar parámetro user
                                ),
                                ft.MenuItemButton(
                                    content=ft.Text("Conoce nuestras instalaciones"),
                                leading=ft.Icon(ft.icons.LOCAL_HOSPITAL),
                                on_click=lambda e: show_facilities(user)
                                ),
                            ]
                        )
                    ]
                    ),
                    padding=10,
                    alignment=ft.alignment.center,
                ),
            ]
        )

        page.controls.clear()
        page.add(
            ft.Row(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(f"Bienvenido, {user[1]} {user[2]}", size=20),
                                ft.ElevatedButton(text="Agende sus citas aquí", on_click=lambda e: show_appointments(user)),
                                ft.ElevatedButton(text="Consulte sus citas aquí", on_click=lambda e: show_user_appointments(user)),
                            ],
                            spacing=15,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.BLACK,
                        width=220,
                        height=900,
                        border_radius=0,
                    ),
                ]
            )
        )
        page.update()

    
    # Página para "Conocer sobre el hospital"
    def show_about(user):
        page.controls.clear()
        page.add(
            ft.AppBar(
            title=ft.Text("Personal del Hospital", color=ft.colors.BLACK, style=ft.TextStyle(font_family="Times New Roman"), weight=ft.FontWeight.BOLD),
            center_title=True,
            bgcolor=ft.colors.BLUE_500,
            )
        )
        page.add(ft.Container(content=ft.Column(
                    controls=[
                        # Bacteriólogos
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Image(src="../Imagenes/Bacteriólogo.jpg", width=400, height=400), margin = ft.margin.only(left=20)
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Bacteriólogos", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text("Personal actual: 14", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text(
                                                "Los bacteriólogos se encargan de analizar muestras biológicas para detectar y diagnosticar enfermedades. Su trabajo es crucial para la identificación de patógenos y la prevención de brotes infecciosos. Ellos trabajan en laboratorios de microbiología, realizando cultivos y pruebas bioquímicas para proporcionar diagnósticos precisos.", 
                                                width=500,
                                                height=400, 
                                                color=ft.colors.BLACK, 
                                                size=20
                                            ),
                                        ],
                                        alignment="start",
                                        spacing=5,
                                    ),
                                ],
                                alignment="start",
                                spacing=20,
                            ),
                            padding=10,
                            margin=10,
                            bgcolor=ft.colors.LIGHT_GREEN_100,
                            border_radius=8,
                        ),
                        # Médicos
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Image(src="../Imagenes/Medico.jpg", width=400, height=400, fit=ft.ImageFit.CONTAIN),margin=ft.margin.only(left=10)
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Médicos", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text("Personal actual: 20", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text(
                                                "Los médicos son profesionales altamente capacitados responsables de la atención primaria, el diagnóstico y el tratamiento de enfermedades. Trabajan en diversas áreas de la medicina, desde la medicina general hasta especialidades como la cardiología, neurología, y más. Los médicos realizan exámenes físicos, prescriben medicamentos, y desarrollan planes de tratamiento personalizados. Además, colaboran con otros profesionales de la salud para asegurar una atención integral y continua.", 
                                                width=500,
                                                height=400, 
                                                color=ft.colors.BLACK, 
                                                size=20
                                            ),
                                        ],
                                        alignment="start",
                                        spacing=5,
                                    ),
                                ],
                                alignment="start",
                                spacing=20,
                            ),
                            padding=10,
                            margin=10,
                            bgcolor=ft.colors.LIGHT_GREEN_100,
                            border_radius=8,
                        ),
                        # Psicólogos
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Image(src="../Imagenes/Psicologo.jpg", width=400, height=400), margin = ft.margin.only(left=20)
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Psicologos", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text("Personal actual: 9", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text(
                                                "Los psicólogos se especializan en el estudio del comportamiento y los procesos mentales. Utilizan diversas técnicas terapéuticas para ayudar a los pacientes a manejar problemas emocionales, conductuales y de salud mental. Los psicólogos trabajan en múltiples entornos, incluidos hospitales, clínicas, escuelas y consultorios privados. A través de evaluaciones y terapias, apoyan a los individuos en la mejora de su bienestar mental y emocional.", 
                                                width=500,
                                                height=400, 
                                                color=ft.colors.BLACK, 
                                                size=20
                                            ),
                                        ],
                                        alignment="start",
                                        spacing=5,
                                    ),
                                ],
                                alignment="start",
                                spacing=20,
                            ),
                            padding=10,
                            margin=10,
                            bgcolor=ft.colors.LIGHT_GREEN_100,
                            border_radius=8,
                        ),
                        # Psiquiatras
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Image(src="../Imagenes/Psiquiatra.jpg", width=400, height=400, fit=ft.ImageFit.CONTAIN), margin=ft.margin.only(left=20)
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Psiquiatras", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text("Personal actual: 8", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text(
                                                "Los psiquiatras son médicos especializados en la salud mental. Se encargan del diagnóstico, tratamiento y prevención de trastornos mentales, emocionales y de comportamiento. A diferencia de los psicólogos, los psiquiatras pueden prescribir medicamentos y ofrecer terapias biológicas junto con tratamientos psicoterapéuticos. Trabajan en estrecha colaboración con otros profesionales de la salud para proporcionar un enfoque integral a la atención de sus pacientes.", 
                                                width=500,
                                                height=400, 
                                                color=ft.colors.BLACK, 
                                                size=20
                                            ),
                                        ],
                                        alignment="start",
                                        spacing=5,
                                    ),
                                ],
                                alignment="start",
                                spacing=20,
                            ),
                            padding=10,
                            margin=10,
                            bgcolor=ft.colors.LIGHT_GREEN_100,
                            border_radius=8,
                        ),
                        # Cirujanos
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Image(src="../Imagenes/Cirujano.jpg", width=400, height=400, fit=ft.ImageFit.CONTAIN), margin=ft.margin.only(left=20)
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Cirujanos", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text("Personal actual: 15", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text(
                                                "Los cirujanos son médicos especializados en realizar intervenciones quirúrgicas para tratar enfermedades, lesiones y deformidades. Con una formación rigurosa y habilidades técnicas avanzadas, los cirujanos operan en diversas especialidades como la cirugía general, ortopédica, cardiovascular, neurológica, entre otras. Además de realizar cirugías, supervisan el proceso de recuperación y seguimiento postoperatorio de los pacientes.", 
                                                width=500,
                                                height=400, 
                                                color=ft.colors.BLACK, 
                                                size=20
                                            ),
                                        ],
                                        alignment="start",
                                        spacing=5,
                                    ),
                                ],
                                alignment="start",
                                spacing=20,
                            ),
                            padding=10,
                            margin=10,
                            bgcolor=ft.colors.LIGHT_GREEN_100,
                            border_radius=8,
                        ),
                        # Pediatras
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Image(src="../Imagenes/Pediatra.jpg", width=400, height=400, fit=ft.ImageFit.CONTAIN), margin=ft.margin.only(left=20)
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Pediatras", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text("Personal actual: 12", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text(
                                                "Los pediatras son médicos especializados en el cuidado de la salud de los niños desde el nacimiento hasta la adolescencia. Ofrecen atención preventiva, diagnóstica y terapéutica para una variedad de enfermedades y condiciones pediátricas. Los pediatras también se enfocan en el desarrollo físico, emocional y social de los niños, asesorando a los padres sobre el bienestar general y el crecimiento saludable de sus hijos.", 
                                                width=500,
                                                height=400, 
                                                color=ft.colors.BLACK, 
                                                size=20
                                            ),
                                        ],
                                        alignment="start",
                                        spacing=5,
                                    ),
                                ],
                                alignment="start",
                                spacing=20,
                            ),
                            padding=10,
                            margin=10,
                            bgcolor=ft.colors.LIGHT_GREEN_100,
                            border_radius=8,
                        ),
                        # Radiólogos
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Image(src="../Imagenes/Radiologos.jpg", width=400, height=400, fit=ft.ImageFit.CONTAIN), margin=ft.margin.only(left=20)
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Radiólogos", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text("Personal actual: 7", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text(
                                                "Los radiólogos son médicos especializados en la interpretación de imágenes médicas para el diagnóstico y tratamiento de enfermedades. Utilizan diversas modalidades de imagen como rayos X, resonancias magnéticas, tomografías computarizadas y ultrasonidos. Los radiólogos juegan un papel crucial en la identificación de condiciones médicas, guiando a otros profesionales de la salud en la planificación del tratamiento adecuado.", 
                                                width=500,
                                                height=400, 
                                                color=ft.colors.BLACK, 
                                                size=20
                                            ),
                                        ],
                                        alignment="start",
                                        spacing=5,
                                    ),
                                ],
                                alignment="start",
                                spacing=20,
                            ),
                            padding=10,
                            margin=10,
                            bgcolor=ft.colors.LIGHT_GREEN_100,
                            border_radius=8,
                        ),
                        # Anestesiólogos
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Image(src="../Imagenes/Anestesiologo.jpg", width=400, height=400, fit=ft.ImageFit.CONTAIN), margin=ft.margin.only(left=20)
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Anestesiólogos", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text("Personal actual: 6", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text(
                                                "Los anestesiólogos son médicos especializados en la administración de anestesia y el manejo del dolor durante y después de procedimientos quirúrgicos. Evalúan a los pacientes antes de la cirugía, administran medicamentos anestésicos y monitorean las funciones vitales durante la operación. También gestionan el dolor postoperatorio y otras condiciones agudas o crónicas relacionadas con el dolor.", 
                                                width=500,
                                                height=400, 
                                                color=ft.colors.BLACK, 
                                                size=20
                                            ),
                                        ],
                                        alignment="start",
                                        spacing=5,
                                    ),
                                ],
                                alignment="start",
                                spacing=20,
                            ),
                            padding=10,
                            margin=10,
                            bgcolor=ft.colors.LIGHT_GREEN_100,
                            border_radius=8,
                        ),
                        # Enfermeros
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Image(src="../Imagenes/Enfermero.jpg", width=400, height=400, fit=ft.ImageFit.CONTAIN), margin=ft.margin.only(left=20)
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Enfermeros", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text("Personal actual: 30", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text(
                                                "Los enfermeros son profesionales de la salud que brindan atención integral a los pacientes en diversos entornos médicos. Desempeñan un papel vital en el seguimiento de la salud de los pacientes, administrando medicamentos, realizando procedimientos, y ofreciendo apoyo emocional. Los enfermeros también educan a los pacientes y sus familias sobre la gestión de enfermedades y la promoción de la salud.", 
                                                width=500,
                                                height=400, 
                                                color=ft.colors.BLACK, 
                                                size=20
                                            ),
                                        ],
                                        alignment="start",
                                        spacing=5,
                                    ),
                                ],
                                alignment="start",
                                spacing=20,
                            ),
                            padding=10,
                            margin=10,
                            bgcolor=ft.colors.LIGHT_GREEN_100,
                            border_radius=8,
                        ),
                        # Fisioterapeutas
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Image(src="../Imagenes/Fisioterapeuta.jpg", width=400, height=400, fit=ft.ImageFit.CONTAIN), margin=ft.margin.only(left=20)
                                    ),
                                    ft.Column(
                                        controls=[
                                            ft.Text("Fisioterapeutas", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text("Personal actual: 5", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                            ft.Text(
                                                "Los fisioterapeutas se especializan en la rehabilitación física y el tratamiento de disfunciones musculoesqueléticas. Utilizan ejercicios terapéuticos, técnicas manuales y modalidades físicas para ayudar a los pacientes a recuperar la movilidad y la funcionalidad. Trabajan con individuos que han sufrido lesiones, cirugías, enfermedades crónicas o discapacidades, desarrollando planes de tratamiento personalizados para mejorar la calidad de vida.", 
                                                width=500,
                                                height=400, 
                                                color=ft.colors.BLACK, 
                                                size=20
                                            ),
                                        ],
                                        alignment="start",
                                        spacing=5,
                                    ),
                                ],
                                alignment="start",
                                spacing=20,
                            ),
                            padding=10,
                            margin=10,
                            bgcolor=ft.colors.LIGHT_GREEN_100,
                            border_radius=8,
                        ),
                    ],
                    alignment="start",
                    spacing=10,
                    scroll=ft.ScrollMode.ALWAYS,  # Aplicar el scroll aquí
                ),
                padding=10,
                expand=True,
            )
        )
        page.add(ft.ElevatedButton(text="Volver al panel de control", on_click=lambda e: dashboard_page(user)))
        page.update()

    # Página para "Ver información sobre las instalaciones"
    def show_facilities(user):
        page.controls.clear()
        page.title = "Conoce las instalaciones de nuestro hospital"
        page.add(ft.AppBar(
            title=ft.Text("Nuestras instalaciones", color=ft.colors.BLACK, style=ft.TextStyle(font_family="Times New Roman"), weight=ft.FontWeight.BOLD),
            center_title=True,
            bgcolor=ft.colors.BLUE_500,
            ),
        )
        page.add (ft.Container(
                    content=ft.Column(
                        controls=[
                            # Bacteriólogos
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=ft.Image(src="../Imagenes/Salaespera.jpg", width=400, height=400), margin = ft.margin.only(left=20)
                                        ),
                                        ft.Column(
                                            controls=[
                                                ft.Text("Recepción y Sala de espera", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                ft.Text("Cantidad: 4 áreas", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                ft.Text(
                                                    "Las áreas de recepción y sala de espera son el primer punto de contacto para los pacientes al llegar al hospital. Aquí, el personal administrativo se encarga de recibir a los pacientes, registrar su información, programar citas y proporcionar orientación sobre los servicios del hospital. Las salas de espera están diseñadas para brindar comodidad a los pacientes y sus familiares mientras esperan su turno para consultas médicas, procedimientos o visitas a pacientes hospitalizados.", 
                                                    width=500,
                                                    height=400, 
                                                    color=ft.colors.BLACK, 
                                                    size=20
                                                ),
                                            ],
                                            alignment="start",
                                            spacing=5,
                                        ),
                                    ],
                                    alignment="start",
                                    spacing=20,
                                ),
                                padding=10,
                                margin=10,
                                bgcolor=ft.colors.LIGHT_GREEN_100,
                                border_radius=8,
                            ),
                            # Médicos
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=ft.Image(src="../Imagenes/Quirofano.jpg", width=400, height=400, fit=ft.ImageFit.CONTAIN),margin=ft.margin.only(left=10)
                                        ),
                                        ft.Column(
                                            controls=[
                                                ft.Text("Quirófanos", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                ft.Text("Cantidad: 6 quirófanos", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                ft.Text(
                                                    " Los quirófanos son espacios altamente especializados diseñados para realizar intervenciones quirúrgicas de manera segura y eficiente. Estas salas están equipadas con tecnología médica avanzada, incluidos equipos de monitorización vital, sistemas de anestesia y herramientas quirúrgicas especializadas. El personal médico y de enfermería altamente capacitado trabaja en equipo para llevar a cabo procedimientos quirúrgicos, asegurando el bienestar del paciente antes, durante y después de la cirugía.", 
                                                    width=500,
                                                    height=400, 
                                                    color=ft.colors.BLACK, 
                                                    size=20
                                                ),
                                            ],
                                            alignment="start",
                                            spacing=5,
                                        ),
                                    ],
                                    alignment="start",
                                    spacing=20,
                                ),
                                padding=10,
                                margin=10,
                                bgcolor=ft.colors.LIGHT_GREEN_100,
                                border_radius=8,
                            ),
                            # Psicólogos
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=ft.Image(src="../Imagenes/Salaconsulta.jpg", width=400, height=400), margin = ft.margin.only(left=20)
                                        ),
                                        ft.Column(
                                            controls=[
                                                ft.Text("Salas de Consulta", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                ft.Text("Cantidad: 12 salas", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                ft.Text(
                                                    "Las salas de consulta son espacios donde los pacientes se reúnen con médicos y especialistas para recibir evaluaciones médicas, diagnósticos y planes de tratamiento. Estas salas están diseñadas para proporcionar un entorno cómodo y privado donde los pacientes pueden discutir sus preocupaciones de salud, recibir orientación médica y participar en decisiones relacionadas con su atención médica. El personal médico utiliza estas salas para realizar exámenes físicos, evaluar síntomas, solicitar pruebas diagnósticas y brindar atención médica personalizada.", 
                                                    width=500,
                                                    height=400, 
                                                    color=ft.colors.BLACK, 
                                                    size=20
                                                ),
                                            ],
                                            alignment="start",
                                            spacing=5,
                                        ),
                                    ],
                                    alignment="start",
                                    spacing=20,
                                ),
                                padding=10,
                                margin=10,
                                bgcolor=ft.colors.LIGHT_GREEN_100,
                                border_radius=8,
                            ),
                            # Psiquiatras
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=ft.Image(src="../Imagenes/Salaradiologia.jpg", width=400, height=400, fit=ft.ImageFit.CONTAIN), margin=ft.margin.only(left=20)
                                        ),
                                        ft.Column(
                                            controls=[
                                                ft.Text("Salas de Radiología", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                ft.Text("Cantidad: 5 salas", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                ft.Text(
                                                    "Las salas de radiología están equipadas con tecnología avanzada de diagnóstico por imágenes para realizar una variedad de estudios radiológicos, como radiografías, tomografías computarizadas (TC), resonancias magnéticas (RM) y ecografías. El personal técnico especializado opera los equipos de radiología para obtener imágenes precisas del interior del cuerpo, que luego son interpretadas por radiólogos y otros médicos para diagnosticar enfermedades y lesiones. Estas salas son fundamentales para la evaluación y el seguimiento de condiciones médicas, ayudando a guiar el tratamiento adecuado de los pacientes.", 
                                                    width=500,
                                                    height=400, 
                                                    color=ft.colors.BLACK, 
                                                    size=20
                                                ),
                                            ],
                                            alignment="start",
                                            spacing=5,
                                        ),
                                    ],
                                    alignment="start",
                                    spacing=20,
                                ),
                                padding=10,
                                margin=10,
                                bgcolor=ft.colors.LIGHT_GREEN_100,
                                border_radius=8,
                            ),
                            # Cirujanos
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=ft.Image(src="../Imagenes/Labclinico.jpg", width=400, height=400, fit=ft.ImageFit.CONTAIN), margin=ft.margin.only(left=20)
                                        ),
                                        ft.Column(
                                            controls=[
                                                ft.Text("Laboratorios Clínicos", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                ft.Text("Cantidad: 3 laboratorios", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                ft.Text(
                                                    " Los laboratorios clínicos son instalaciones donde se realizan pruebas y análisis de muestras biológicas, como sangre, orina y tejidos, para el diagnóstico y monitoreo de enfermedades. El personal técnico cualificado lleva a cabo una amplia gama de pruebas, incluidos análisis de sangre, cultivos microbiológicos, pruebas de función renal y estudios genéticos, utilizando equipos especializados y técnicas de laboratorio avanzadas. Los resultados de los análisis clínicos proporcionan información valiosa para los médicos en la evaluación de la salud de los pacientes y la planificación de su tratamiento.", 
                                                    width=500,
                                                    height=400, 
                                                    color=ft.colors.BLACK, 
                                                    size=20
                                                ),
                                            ],
                                            alignment="start",
                                            spacing=5,
                                        ),
                                    ],
                                    alignment="start",
                                    spacing=20,
                                ),
                                padding=10,
                                margin=10,
                                bgcolor=ft.colors.LIGHT_GREEN_100,
                                border_radius=8,
                            ),
                            # Pediatras
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=ft.Image(src="../Imagenes/UCI.jpg", width=400, height=400, fit=ft.ImageFit.CONTAIN), margin=ft.margin.only(left=20)
                                        ),
                                        ft.Column(
                                            controls=[
                                                ft.Text("Unidad de Cuidados Intensivos (UCI)", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                ft.Text("Cantidad: 2 unidades", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                ft.Text(
                                                    " La Unidad de Cuidados Intensivos es un área especializada del hospital destinada a pacientes que requieren atención médica intensiva y monitoreo continuo debido a condiciones médicas críticas o procedimientos postoperatorios complejos. Equipada con tecnología médica avanzada, como ventiladores mecánicos, monitores cardíacos y sistemas de soporte vital, la UCI brinda atención especializada y vigilancia constante por parte de un equipo multidisciplinario de médicos, enfermeras y personal de apoyo. Esta unidad se centra en estabilizar la condición del paciente y proporcionar cuidados intensivos para promover la recuperación.", 
                                                    width=500,
                                                    height=400, 
                                                    color=ft.colors.BLACK, 
                                                    size=20
                                                ),
                                            ],
                                            alignment="start",
                                            spacing=5,
                                        ),
                                    ],
                                    alignment="start",
                                    spacing=20,
                                ),
                                padding=10,
                                margin=10,
                                bgcolor=ft.colors.LIGHT_GREEN_100,
                                border_radius=8,
                            ),
                            # Radiólogos
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=ft.Image(src="../Imagenes/Rehabilitacion.jpg", width=400, height=400, fit=ft.ImageFit.CONTAIN), margin=ft.margin.only(left=20)
                                        ),
                                        ft.Column(
                                            controls=[
                                                ft.Text("Salas de Rehabilitación", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                ft.Text("Cantidad: 5 salas", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                ft.Text(
                                                    "Las salas de rehabilitación son espacios diseñados para proporcionar terapia física, ocupacional y de rehabilitación a pacientes que se están recuperando de lesiones, cirugías o enfermedades que afectan su movilidad y funcionalidad. Equipadas con equipos especializados y áreas de ejercicio, estas salas ofrecen programas de rehabilitación personalizados dirigidos por fisioterapeutas y terapeutas ocupacionales. Los pacientes participan en ejercicios terapéuticos, entrenamiento de movilidad y actividades funcionales para mejorar su fuerza, flexibilidad y capacidad para realizar actividades cotidianas.", 
                                                    width=500,
                                                    height=400, 
                                                    color=ft.colors.BLACK, 
                                                    size=20
                                                ),
                                            ],
                                            alignment="start",
                                            spacing=5,
                                        ),
                                    ],
                                    alignment="start",
                                    spacing=20,
                                ),
                                padding=10,
                                margin=10,
                                bgcolor=ft.colors.LIGHT_GREEN_100,
                                border_radius=8,
                            ),
                            # Anestesiólogos
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=ft.Image(src="../Imagenes/Salaemergencia.jpg", width=400, height=400, fit=ft.ImageFit.CONTAIN), margin=ft.margin.only(left=20)
                                        ),
                                        ft.Column(
                                            controls=[
                                                ft.Text("Sala de Emergencias", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                ft.Text("Cantidad: 1 sala de emergencias principal", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                ft.Text(
                                                    " La sala de emergencias es un área vital del hospital dedicada a la evaluación y estabilización de pacientes que presentan condiciones médicas agudas, lesiones traumáticas o emergencias médicas repentinas. Operada por un equipo médico altamente capacitado, que incluye médicos de emergencia, enfermeras y personal de apoyo, la sala de emergencias está equipada para manejar una amplia gama de situaciones de emergencia, como ataques cardíacos, accidentes cerebrovasculares, traumas graves y envenenamientos. Esta sala prioriza la atención rápida y efectiva para salvar vidas y minimizar el impacto de las emergencias médicas.", 
                                                    width=500,
                                                    height=400, 
                                                    color=ft.colors.BLACK, 
                                                    size=20
                                                ),
                                            ],
                                            alignment="start",
                                            spacing=5,
                                        ),
                                    ],
                                    alignment="start",
                                    spacing=20,
                                ),
                                padding=10,
                                margin=10,
                                bgcolor=ft.colors.LIGHT_GREEN_100,
                                border_radius=8,
                            ),
                            # Enfermeros
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=ft.Image(src="../Imagenes/Farmacia.jpg", width=400, height=400, fit=ft.ImageFit.CONTAIN), margin=ft.margin.only(left=20)
                                        ),
                                        ft.Column(
                                            controls=[
                                                ft.Text("Farmacia Hospitalaria", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                ft.Text("Cantidad: 1 farmacia central", style="headlineSmall", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                                                ft.Text(
                                                    "La farmacia hospitalaria es un componente esencial del hospital que se encarga de la preparación, dispensación y distribución segura de medicamentos a los pacientes hospitalizados, así como la gestión de inventarios y la supervisión del uso adecuado de medicamentos. Dirigida por farmacéuticos clínicos, la farmacia hospitalaria garantiza la disponibilidad de medicamentos necesarios, la precisión en las dosis y la compatibilidad de los tratamientos con las necesidades individuales de cada paciente. Además, ofrece servicios de consulta y educación sobre medicamentos para pacientes y profesionales de la salud.", 
                                                    width=500,
                                                    height=400, 
                                                    color=ft.colors.BLACK, 
                                                    size=20
                                                ),
                                            ],
                                            alignment="start",
                                            spacing=5,
                                        ),
                                    ],
                                    alignment="start",
                                    spacing=20,
                                ),
                                padding=10,
                                margin=10,
                                bgcolor=ft.colors.LIGHT_GREEN_100,
                                border_radius=8,
                            ),
                        ],
                        alignment="start",
                        spacing=10,
                        scroll=ft.ScrollMode.ALWAYS,  # Aplicar el scroll aquí
                    ),
                    padding=10,
                    expand=True,
                )
        ),
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
            first_date=datetime.datetime(2024, 5, 21),
            last_date=datetime.datetime(2024, 6, 30),
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
                SELECT * FROM appointments WHERE doctor_id = ? AND date = ? AND time = ?
            ''', (int(doctor_id.value), date_picker.value, time_picker.value))
            appointment_conflict = c.fetchone()

            if appointment_conflict:
                show_alert("Error", "Ya hay una cita programada para este horario con el doctor seleccionado")
            else:
                c.execute('''
                    INSERT INTO appointments (user_id, doctor_id, date, time) VALUES (?, ?, ?, ?)
                ''', (user[0], int(doctor_id.value), date_picker.value, time_picker.value))
                conn.commit()
                show_alert("Éxito", "Cita agendada exitosamente")
            conn.close()
        
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
                    nombre_completo = f"{appointment[0]} {appointment[1]}"
                    fecha = appointment[2]
                    hora = appointment[3]

                    card = ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.Text(f"Paciente: {nombre_completo}", weight="bold", size=18),
                                ft.Text(f"Fecha: {fecha}"),
                                ft.Text(f"Hora: {hora}"),
                            ]),
                            padding=10,
                        ),
                        elevation=2,
                    )

                    page.add(card)
        else:
            page.add(ft.Text("No tienes citas programadas"))
        
        page.add(ft.ElevatedButton(text="Volver al panel de control", on_click=lambda e: doctor_dashboard(doctor)))
        page.update()
    
    # Página para "Ver mis citas" como usuario
    def show_user_appointments(user):
        page.controls.clear()
        page.add(ft.Text("Mis Citas", size=20))
        
        conn = sqlite3.connect('database_hospital.db')
        c = conn.cursor()
        c.execute('''
            SELECT doctors.nombre, appointments.date, appointments.time
            FROM appointments
            INNER JOIN doctors ON appointments.doctor_id = doctors.id
            WHERE user_id = ?
        ''', (user[0],))
        appointments = c.fetchall()
        conn.close()
        
        if appointments:
            for appointment in appointments:
                nombre_doctor = appointment[0]
                fecha = appointment[1]
                hora = appointment[2]

                card = ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text(f"Doctor: {nombre_doctor}", weight="bold", size=18),
                            ft.Text(f"Fecha: {fecha}"),
                            ft.Text(f"Hora: {hora}"),
                        ]),
                        padding=10,
                    ),
                    elevation=2,
                )

                page.add(card)
        else:
            page.add(ft.Text("No tienes citas programadas"))
        
        page.add(ft.ElevatedButton(text="Volver al panel de control", on_click=lambda e: dashboard_page(user)))
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