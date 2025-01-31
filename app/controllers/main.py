from flask import Blueprint, render_template

main = Blueprint('main',__name__,template_folder='ruta_a_tu_carpeta_templates')

@main.route('/')
def index():
    """
    Renderiza la página principal del sistema.
    """
    return render_template('index.html')

