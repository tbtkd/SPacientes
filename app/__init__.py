from flask import Flask
from app.db import init_db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
    
    # Configuración de cookies
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
    app.config['SESSION_COOKIE_SECURE'] = True  # Solo para producción (HTTPS)
    
    with app.app_context():
        init_db()
        
    from app.controllers.main import main
    from app.controllers.pacientes import pacientes
    from app.controllers.historial_clinico import historial_clinico
    from app.controllers.valoracion_antropometrica import valoracion
    app.register_blueprint(main)
    app.register_blueprint(pacientes)
    app.register_blueprint(historial_clinico)
    app.register_blueprint(valoracion)
    
    return app

