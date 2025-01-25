from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db import get_db, query_db, get_historial_clinico, crear_historial_clinico, actualizar_historial_clinico

historial_clinico = Blueprint('historial_clinico', __name__)

@historial_clinico.route('/pacientes/<int:paciente_id>/historial-clinico', methods=['GET', 'POST'])
def ver_crear_historial(paciente_id):
    paciente = query_db('SELECT * FROM pacientes WHERE id = ?', [paciente_id], one=True)
    if not paciente:
        flash('Paciente no encontrado', 'error')
        return redirect(url_for('pacientes.lista_pacientes'))

    historial = get_historial_clinico(paciente_id)

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
            actualizar_historial_clinico(paciente_id, datos)
            flash('Historial clínico actualizado exitosamente', 'success')
        else:
            crear_historial_clinico(paciente_id, datos)
            flash('Historial clínico creado exitosamente', 'success')

        return redirect(url_for('historial_clinico.ver_crear_historial', paciente_id=paciente_id))

    padecimientos_opciones = [
        'Gastritis', 'Colitis', 'Reflujo', 'Estreñimiento', 'Diarrea',
        'Hemorroides', 'Intolerancias', 'Alergias', 'Diabetes',
        'Dislipidemias', 'Presión arterial', 'Otro descontrol metabólico'
    ]

    return render_template('historial_clinico.html', paciente=paciente, historial=historial, padecimientos_opciones=padecimientos_opciones)

@historial_clinico.route('/historial-clinico')
def lista_historiales():
    historiales = query_db('''
        SELECT h.*, p.nombre, p.apellido_paterno, p.apellido_materno
        FROM historial_clinico h
        JOIN pacientes p ON h.paciente_id = p.id
    ''')
    return render_template('lista_historiales.html', historiales=historiales)

