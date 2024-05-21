import flet as ft

def VerPantallaPersonal(page: ft.Page):
    page.title = "Conoce el personal de nuestro hospital"
    ft.View(appbar=ft.AppBar(
            title=ft.Text("Personal del Hospital", color=ft.colors.BLACK, style=ft.TextStyle(font_family="Times New Roman"), weight=ft.FontWeight.BOLD),
            center_title=True,
            bgcolor=ft.colors.BLUE_400,
        ),
        controls=[
            ft.Container(
                content=ft.Column(
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
        ]
    )
