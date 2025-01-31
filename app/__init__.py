from flask import Flask
from app.db import init_db

def create_app(config_name='default'):  # Agregamos parámetro para diferentes configuraciones
    """
    Función factory para crear y configurar la aplicación Flask
    Args:
        config_name (str): Nombre de la configuración a utilizar (default, development, production)
    Returns:
        Flask: Aplicación Flask configurada
    """
    # Inicialización de la aplicación Flask
    app = Flask(__name__)
    
    # Configuración básica de seguridad
    app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'  # TODO: Mover a variables de entorno
    
    # Configuración de cookies para mayor seguridad
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # Protección contra ataques CSRF
    app.config['SESSION_COOKIE_SECURE'] = True      # Asegura cookies solo por HTTPS
    app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # Sesión expira en 30 minutos
    
    # Inicialización de la base de datos
    with app.app_context():
        init_db()
    
    # Registro de blueprints (módulos de la aplicación)
    from app.controllers.main import main
    from app.controllers.pacientes import pacientes
    from app.controllers.historial_clinico import historial_clinico
    from app.controllers.valoracion_antropometrica import valoracion
    
    blueprints = [
        main,
        pacientes,
        historial_clinico,
        valoracion
    ]
    
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    
    return app

