import flet as ft

def VerPantallaInstalaciones(page: ft.Page):
    def volver_atras(e):
        page.views.pop()
        page.update()
    page.title = "Conoce las instalaciones de nuestro hospital"
    return ft.View(
        appbar=ft.AppBar(
            title=ft.Text("Nuestras instalaciones", color=ft.colors.BLACK, style=ft.TextStyle(font_family="Times New Roman"), weight=ft.FontWeight.BOLD),
            center_title=True,
            bgcolor=ft.colors.RED_300,
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
        ]
    )