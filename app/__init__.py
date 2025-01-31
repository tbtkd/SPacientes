import os
from flask import Flask
from app.db import init_db
from app.config import config
from app.logger import setup_logger

def create_app(config_name=None):
    """
    Función factory para crear y configurar la aplicación Flask
    Args:
        config_name (str): Nombre de la configuración a utilizar (default, development, production)
    Returns:
        Flask: Aplicación Flask configurada
    """
    # Determinar la configuración a usar
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
    
    # Inicialización de la aplicación Flask
    app = Flask(__name__)
    
    # Cargar configuración
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    # Configurar sistema de logging
    setup_logger(app, config[config_name])
    
    # Inicialización de la base de datos
    try:
        with app.app_context():
            app.logger.info('Inicializando base de datos...')
            init_db()
            app.logger.info('Base de datos inicializada correctamente')
    except Exception as e:
        app.logger.error(f'Error al inicializar la base de datos: {e}')
        raise
    
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
        app.logger.debug(f'Blueprint registrado: {blueprint.name}')
    
    return app