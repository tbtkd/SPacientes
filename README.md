## Sistema de Gestión de Pacientes (V1.1)

Este proyecto es un sistema de gestión de pacientes desarrollado con Python, Flask y SQLite, siguiendo el patrón de diseño MVC.

## Características

* Gestión de Pacientes:
  - Registro de pacientes con los siguientes campos:
    * Nombre
    * Apellido Paterno
    * Apellido Materno
    * Fecha de nacimiento
    * Teléfono
    * Correo
    * Ciudad
  - Consulta y actualización de información de pacientes

* Historial Clínico:
  - Registro y consulta de historial médico
  - Gestión de valoraciones antropométricas

* Base de Datos:
  - SQLite como almacenamiento principal
  - Archivo schema.sql para definición del esquema

* Interfaz Web:
  - Diseño responsivo
  - Validaciones en el lado del cliente con JavaScript

* Estructura del Proyecto:
  - app/controllers/ → Controladores de la aplicación
  - app/models/ → Modelos de datos
  - app/db.py → Configuración de la base de datos
  - run.py → Archivo de ejecución principal
  - requirements.txt → Dependencias del proyecto

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


## Instalación y Uso

1. Clonar el repositorio:
  * git clone <repo_url>
  * cd SistemaPacientes

2. Instalar dependencias:
  * pip install -r requirements.txt

3. Iniciar la aplicación:
  * python run.py

## Mejoras Futuras
  * Implementación de autenticación de usuarios
  * Reportes y estadísticas de pacientes
  * Integración con una API externa para geolocalización de pacientes