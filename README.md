## pip freeze > requirements.txt 

## Sistema de Gestión de Pacientes Nutriológicos

## Descripción
Sistema web para la gestión de pacientes de nutrición, que permite el registro y seguimiento de valoraciones antropométricas, historiales clínicos y control de citas.

## Características Principales
- Gestión de pacientes (alta, baja, consulta)
- Registro de valoraciones antropométricas
- Historial clínico
- Importación de datos desde Excel
- Seguimiento de medidas y progreso
- Interfaz responsiva

## Estructura del Proyecto
sistema_pacientes/
├── app/
│ ├── controllers/ # Controladores de la aplicación
│ ├── models/ # Modelos de datos
│ ├── static/ # Archivos estáticos (CSS, JS, imágenes)
│ │ ├── css/
│ │ ├── js/
│ │ └── img/
│ ├── templates/ # Plantillas HTML
│ └── init.py # Inicialización de la aplicación
├── instance/ # Base de datos SQLite
├── tests/ # Pruebas unitarias
├── venv/ # Entorno virtual (no incluido en repositorio)
├── .gitignore
├── config.py # Configuraciones
├── README.md
├── requirements.txt # Dependencias
└── run.py # Script de inicio


## Configuración del Entorno

### Requisitos Previos
- Python 3.8+
- pip (gestor de paquetes de Python)

### Instalación
1. Clonar el repositorio:

 * git clone [url-del-repositorio]
 * cd sistema_pacientes

2. Crear y activar entorno virtual:

  * python -m venv venv
  * source venv/bin/activate # Linux/Mac
  * venv\Scripts\activate # Windows

3. Instalar dependencias:

  * pip install -r requirements.txt

4. Configurar variables de entorno:

  * Linux/Mac
    - export FLASK_ENV=development # o production
    - export FLASK_APP=run.py

  * Windows
    - set FLASK_ENV=development
    - set FLASK_APP=run.py

### Ejecución
- Desarrollo:

  * Linux/Mac
    - ./run_dev.sh

  * Windows
    - run_dev.bat

## Cambios entre Desarrollo y Producción

### Para Desarrollo:
1. En `config.py`: Usar `DevelopmentConfig`
2. En `__init__.py`: Descomentar configuración de logging
3. Activar `DEBUG = True`
4. Usar base de datos de desarrollo

### Para Producción:
1. En `config.py`: Usar `ProductionConfig`
2. En `__init__.py`: Mantener comentada la configuración de logging
3. Asegurar `DEBUG = False`
4. Usar base de datos de producción
5. Configurar `SECRET_KEY` segura

## Mantenimiento
- Base de datos: SQLite (puede cambiarse a otro motor si se requiere)
- Logs: Desactivados por defecto, activar en desarrollo si se necesita
- Caché: Implementada para optimizar consultas frecuentes

## Seguridad
- Sesiones seguras configuradas
- Validación de datos en frontend y backend
- Protección contra CSRF
- Sanitización de entradas de usuario

## Contribución
1. Fork del repositorio
2. Crear rama para nueva característica
3. Commit de cambios
4. Push a la rama
5. Crear Pull Request

## Licencia
[Especificar licencia]