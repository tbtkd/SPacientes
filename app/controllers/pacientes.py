from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db import get_db, query_db, obtener_ultimo_pago, actualizar_estatus_paciente, registrar_pago
import sqlite3
from datetime import datetime

pacientes = Blueprint('pacientes', __name__)

@pacientes.route('/pacientes/nuevo', methods=['GET', 'POST'])
def nuevo_paciente():
    if request.method == 'POST':
        db = get_db()
        try:
            db.execute(
                'INSERT INTO pacientes (nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono, correo, ciudad, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                (request.form['nombre'], request.form['apellido_paterno'], request.form['apellido_materno'],
                request.form['fecha_nacimiento'], request.form['telefono'], request.form['correo'], request.form['ciudad'], 'Activo')
            )
            db.commit()
            flash('Paciente registrado exitosamente', 'success')
            return redirect(url_for('pacientes.lista_pacientes'))
        except sqlite3.IntegrityError:
            flash('Error: El correo electrónico ya está registrado', 'error')
        except Exception as e:
            flash(f'Error al registrar el paciente: {str(e)}', 'error')
    return render_template('nuevo_paciente.html')

@pacientes.route('/pacientes')
def lista_pacientes():
    pacientes = query_db('''
        SELECT p.*, 
            (SELECT fecha_pago FROM pagos WHERE paciente_id = p.id ORDER BY fecha_pago DESC LIMIT 1) as ultimo_pago
        FROM pacientes p
    ''')
    return render_template('lista_pacientes.html', pacientes=pacientes)

@pacientes.route('/pacientes/<int:id>')
def detalle_paciente(id):
    paciente = query_db('SELECT * FROM pacientes WHERE id = ?', [id], one=True)
    if paciente is None:
        flash('Paciente no encontrado', 'error')
        return redirect(url_for('pacientes.lista_pacientes'))
    ultimo_pago = obtener_ultimo_pago(id)
    return render_template('detalle_paciente.html', paciente=paciente, ultimo_pago=ultimo_pago)

@pacientes.route('/pacientes/<int:id>/editar', methods=['GET', 'POST'])
def editar_paciente(id):
    paciente = query_db('SELECT * FROM pacientes WHERE id = ?', [id], one=True)
    if paciente is None:
        flash('Paciente no encontrado', 'error')
        return redirect(url_for('pacientes.lista_pacientes'))
    
    if request.method == 'POST':
        db = get_db()
        try:
            db.execute(
                'UPDATE pacientes SET nombre = ?, apellido_paterno = ?, apellido_materno = ?, fecha_nacimiento = ?, telefono = ?, correo = ?, ciudad = ?, status = ? WHERE id = ?',
                (request.form['nombre'], request.form['apellido_paterno'], request.form['apellido_materno'],
                request.form['fecha_nacimiento'], request.form['telefono'], request.form['correo'], 
                request.form['ciudad'], request.form['estatus'], id)
            )
            db.commit()
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
    registrar_pago(id, fecha_pago)
    flash('Pago registrado exitosamente', 'success')
    return redirect(url_for('pacientes.detalle_paciente', id=id))

