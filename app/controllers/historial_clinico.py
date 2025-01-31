from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.paciente import Paciente
from app.models.historial_clinico import HistorialClinico

historial_clinico = Blueprint('historial_clinico', __name__, url_prefix='/historial-clinico')

@historial_clinico.route('/paciente/<int:paciente_id>', methods=['GET', 'POST'])
def ver_crear_historial(paciente_id):
    paciente = Paciente.obtener_por_id(paciente_id)
    if not paciente:
        flash('Paciente no encontrado', 'error')
        return redirect(url_for('pacientes.lista_pacientes'))

    historial = HistorialClinico.obtener_por_paciente_id(paciente_id)

    if request.method == 'POST':
        datos = {
            'cirugias': request.form['cirugias'],
            'padecimientos': ','.join(request.form.getlist('padecimientos')),
            'medicamentos': request.form['medicamentos'],
            'suplementos': request.form['suplementos'],
            'enfermedades_previas': request.form['enfermedades_previas'],
            'enfermedades_actuales': request.form['enfermedades_actuales'],
            'tipo_actividad_fisica': request.form['tipo_actividad_fisica'],
            'frecuencia_actividad_fisica': request.form['frecuencia_actividad_fisica'],
            'tiempo_actividad_fisica': request.form['tiempo_actividad_fisica'],
            'numero_comidas_diarias': request.form['numero_comidas_diarias'],
            'alimentos_normales': request.form['alimentos_normales'],
            'alimentos_no_gustados': request.form['alimentos_no_gustados']
        }

        if historial:
            HistorialClinico.actualizar(paciente_id, datos)
            flash('Historial clínico actualizado exitosamente', 'success')
        else:
            HistorialClinico.crear(paciente_id, datos)
            flash('Historial clínico creado exitosamente', 'success')

        return redirect(url_for('historial_clinico.ver_crear_historial', paciente_id=paciente_id))

    padecimientos_opciones = [
        'Gastritis', 'Colitis', 'Reflujo', 'Estreñimiento', 'Diarrea',
        'Hemorroides', 'Intolerancias', 'Alergias', 'Diabetes',
        'Dislipidemias', 'Presión arterial', 'Otro descontrol metabólico'
    ]

    return render_template('historiales/historial_clinico.html', paciente=paciente, historial=historial, padecimientos_opciones=padecimientos_opciones)

@historial_clinico.route('/')
def lista_historiales():
    historiales = HistorialClinico.obtener_todos()
    return render_template('historiales/lista_historiales.html', historiales=historiales)

