from app.db import get_db, query_db
from datetime import datetime
import sqlite3

class Paciente:
    @staticmethod
    def crear(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono, correo, ciudad):
        """
        Crea un nuevo paciente en la base de datos
        Args:
            nombre (str): Nombre del paciente
            apellido_paterno (str): Apellido paterno del paciente
            apellido_materno (str): Apellido materno del paciente
            fecha_nacimiento (str): Fecha de nacimiento del paciente
            telefono (str): Teléfono del paciente
            correo (str): Correo electrónico del paciente
            ciudad (str): Ciudad del paciente
        Returns:
            int: ID del paciente creado
        """
        try:
            # Verificar si el correo ya existe
            existente = query_db('SELECT id FROM pacientes WHERE correo = ?', [correo], one=True)
            if existente:
                raise Exception("El correo electrónico ya está registrado")
            
            db = get_db()
            # Primero insertamos el paciente
            db.execute(
            'INSERT INTO pacientes (nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono, correo, ciudad) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono, correo, ciudad)
            )
            db.commit()
            
            # Obtener el ID del paciente recién creado usando lastrowid
            paciente_id = db.execute('SELECT last_insert_rowid()').fetchone()[0]
            return paciente_id
            
        except Exception as e:
            db.rollback() if 'db' in locals() else None
            raise e

    @staticmethod
    def obtener_todos():
        return query_db('''
            SELECT p.*, 
                    (SELECT fecha_pago FROM pagos WHERE paciente_id = p.id ORDER BY fecha_pago DESC LIMIT 1) as ultimo_pago
            FROM pacientes p
        ''')

    @staticmethod
    def obtener_por_id(id):
        return query_db('SELECT * FROM pacientes WHERE id = ?', [id], one=True)

    @staticmethod
    def actualizar(id, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono, correo, ciudad, status):
        db = get_db()
        db.execute(
            'UPDATE pacientes SET nombre = ?, apellido_paterno = ?, apellido_materno = ?, fecha_nacimiento = ?, telefono = ?, correo = ?, ciudad = ?, status = ? WHERE id = ?',
            (nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono, correo, ciudad, status, id)
        )
        db.commit()

    @staticmethod
    def actualizar_estatus(paciente_id, status):
        db = get_db()
        db.execute('UPDATE pacientes SET estatus = ? WHERE id = ?', (status, paciente_id))
        db.commit()

    @staticmethod
    def buscar(busqueda):
        return query_db('''
            SELECT p.*, 
                    (SELECT fecha_pago FROM pagos WHERE paciente_id = p.id ORDER BY fecha_pago DESC LIMIT 1) as ultimo_pago
            FROM pacientes p
            WHERE p.nombre LIKE ? OR p.apellido_paterno LIKE ? OR p.apellido_materno LIKE ?
            ORDER BY p.nombre, p.apellido_paterno, p.apellido_materno
        ''', ['%' + busqueda + '%'] * 3)