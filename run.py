import webbrowser
import threading
import time
import requests
import logging
from app import create_app

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuración de la aplicación
PORT = 5000
HOST = 'localhost'
MAX_RETRIES = 30  # 30 segundos máximo de espera

def run_flask():
    try:
        app = create_app()
        app.run(host=HOST, port=PORT, debug=False)
    except Exception as e:
        logger.error(f"Error al iniciar Flask: {e}")
        raise

def open_browser():
    url = f'http://{HOST}:{PORT}/'
    try:
        webbrowser.open_new(url)
        logger.info("Navegador web abierto exitosamente")
    except Exception as e:
        logger.error(f"Error al abrir el navegador: {e}")

def check_flask_status():
    url = f'http://{HOST}:{PORT}/'
    retries = 0
    
    while retries < MAX_RETRIES:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                logger.info("Servidor Flask iniciado correctamente")
                return True
        except requests.ConnectionError:
            retries += 1
            time.sleep(1)
            logger.debug(f"Intentando conectar al servidor... ({retries}/{MAX_RETRIES})")
    
    logger.error("No se pudo iniciar el servidor Flask")
    return False

def shutdown_server():
    logger.info("Cerrando el servidor...")
    try:
        requests.get(f'http://{HOST}:{PORT}/shutdown', timeout=2)
    except Exception as e:
        logger.debug(f"Error al cerrar el servidor: {e}")

if __name__ == '__main__':
    flask_thread = None
    try:
        logger.info("Iniciando la aplicación...")
        flask_thread = threading.Thread(target=run_flask)
        flask_thread.daemon = True
        flask_thread.start()

        if check_flask_status():
            open_browser()
        else:
            logger.error("La aplicación no pudo iniciarse correctamente")
            exit(1)

        # Mantener el programa principal ejecutándose
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        logger.info("Aplicación cerrada por el usuario")
        shutdown_server()
        # Asegurar que el programa termine
        import os
        os._exit(0)
    except Exception as e:
        logger.error(f"Error inesperado: {e}")
        shutdown_server()
        exit(1)

