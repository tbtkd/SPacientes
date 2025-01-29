from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.paciente import Paciente
from app.models.pago import Pago
from app.models.historial_clinico import HistorialClinico
import sqlite3

pacientes = Blueprint('pacientes', __name__)

@pacientes.route('/pacientes/nuevo', methods=['GET', 'POST'])
def nuevo_paciente():
    if request.method == 'POST':
        try:
            Paciente.crear(
                request.form['nombre'], request.form['apellido_paterno'], 
                request.form['apellido_materno'], request.form['fecha_nacimiento'], 
                request.form['telefono'], request.form['correo'], request.form['ciudad']
            )
            flash('Paciente registrado exitosamente', 'success')
            return redirect(url_for('pacientes.lista_pacientes'))
        except sqlite3.IntegrityError:
            flash('Error: El correo electrónico ya está registrado', 'error')
        except Exception as e:
            flash(f'Error al registrar el paciente: {str(e)}', 'error')
    return render_template('nuevo_paciente.html')

@pacientes.route('/pacientes')
def lista_pacientes():
    busqueda = request.args.get('busqueda', '')
    pacientes = Paciente.buscar(busqueda)
    return render_template('lista_pacientes.html', pacientes=pacientes, busqueda=busqueda)

@pacientes.route('/pacientes/<int:id>')
def detalle_paciente(id):
    paciente = Paciente.obtener_por_id(id)
    if paciente is None:
        flash('Paciente no encontrado', 'error')
        return redirect(url_for('pacientes.lista_pacientes'))
    ultimo_pago = Pago.obtener_ultimo_pago(id)
    historial = HistorialClinico.obtener_por_paciente_id(id)
    return render_template('detalle_paciente.html', 
                         paciente=paciente, 
                         ultimo_pago=ultimo_pago,
                         historial=historial)

@pacientes.route('/pacientes/<int:id>/editar', methods=['GET', 'POST'])
def editar_paciente(id):
    paciente = Paciente.obtener_por_id(id)
    if paciente is None:
        flash('Paciente no encontrado', 'error')
        return redirect(url_for('pacientes.lista_pacientes'))
    
    if request.method == 'POST':
        try:
            Paciente.actualizar(
                id, request.form['nombre'], request.form['apellido_paterno'], 
                request.form['apellido_materno'], request.form['fecha_nacimiento'], 
                request.form['telefono'], request.form['correo'], 
                request.form['ciudad'], request.form['estatus']
            )
            flash('Información del paciente actualizada exitosamente', 'success')
            return redirect(url_for('pacientes.detalle_paciente', id=id))
        except sqlite3.IntegrityError:
            flash('Error: El correo electrónico ya está registrado', 'error')
        except Exception as e:
            flash(f'Error al actualizar el paciente: {str(e)}', 'error')
    return render_template('editar_paciente.html', paciente=paciente)

@pacientes.route('/pacientes/<int:id>/pago', methods=['POST'])
def registrar_pago_paciente(id):
    fecha_pago = request.form['fecha_pago']
    Pago.registrar(id, fecha_pago)
    flash('Pago registrado exitosamente', 'success')
    return redirect(url_for('pacientes.detalle_paciente', id=id))

