import os
import webbrowser
from threading import Timer
from app import create_app

def open_browser(port):
    """Abre el navegador predeterminado en la URL de la aplicación"""
    webbrowser.open(f'http://127.0.0.1:{port}/')

app = create_app(os.getenv('FLASK_ENV', 'default'))

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    
    # Programa la apertura del navegador después de 1.5 segundos
    # para dar tiempo a que Flask inicie
    Timer(1.5, open_browser, args=[port]).start()
    
    # Cambiamos host a 127.0.0.1 para mejor compatibilidad con exe
    app.run(
        host='127.0.0.1',
        port=port,
        debug=(os.getenv('FLASK_ENV') == 'development')
    )
