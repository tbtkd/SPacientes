import webbrowser
import threading
import time
import requests
from app import create_app

app = create_app()

def run_flask():
    app.run(debug=False)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

def check_flask_status():
    while True:
        try:
            response = requests.get('http://127.0.0.1:5000/')
            if response.status_code == 200:
                return True
        except requests.ConnectionError:
            time.sleep(0.1)

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    check_flask_status()
    open_browser()

    try:
        flask_thread.join()
    except KeyboardInterrupt:
        print("Aplicación cerrada por el usuario.")

