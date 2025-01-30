# Sistema de Alta de Pacientes (V52)

Este proyecto es un sistema de gestión de pacientes desarrollado con Python, Flask y SQLite, siguiendo el patrón de diseño MVC.

## Características

- Alta de pacientes con los siguientes campos:
  - Nombre
  - Apellido Paterno
  - Apellido Materno
  - Fecha de nacimiento
  - Teléfono
  - Correo
  - Ciudad
- Consulta de usuarios registrados
- Actualización de información de usuarios
- Diseño web responsivo
- Validaciones en el lado del cliente con JavaScript
- Menú desplegable responsivo

## Estructura del Proyecto

📁 Sistemapacientes
│── 📁 static
│   │── 📁 css
│   │   │── style.css                # Nuevo diseño mejorado
│   │   │── forms.css                 # Nuevo diseño para formularios
│   │   └── sidebar.css               # Sidebar fijo
│   │── 📁 js
│   │   └── scripts.js                # Scripts adicionales si es necesario
│   │── 📁 img
│   │   └── logo.png                   # Logo del proyecto
│
│── 📁 templates
│   │── base.html                      # Base general con sidebar fijo
│   │── index.html                      # Página de inicio
│   │── lista_pacientes.html           # Lista de pacientes con nuevo diseño
│   │── nuevo_paciente.html            # Formulario con nuevo diseño
│   │── nueva_valoracion.html          # Formulario con nuevo diseño
│   │── historial_clinico.html         # Formulario con nuevo diseño
│   │── editar_paciente.html           # Formulario con nuevo diseño
│   │── detalle_paciente.html          # Sección de detalle con mejora visual
│   │── detalle_valoracion.html        # Sección con grid mejorado
│
│── 📁 database
│   │── conexion.py                    # Conexión a la base de datos sin SQLAlchemy
│   │── queries.py                      # Consultas SQL estructuradas
│
│── 📁 routes
│   │── views.py                        # Rutas generales
│   │── pacientes.py                    # Módulo de pacientes
│   │── valoraciones.py                 # Módulo de valoraciones
│
│── 📁 static
│   └── 📁 fonts                        # Si se usan fuentes personalizadas
│
│── app.py                              # Punto de entrada del proyecto
│── requirements.txt                     # Dependencias necesarias
│── README.md                            # Documentación general