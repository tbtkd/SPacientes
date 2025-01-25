import sqlite3
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            'pacientes.db',
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    db.commit()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def get_historial_clinico(paciente_id):
    return query_db('SELECT * FROM historial_clinico WHERE paciente_id = ?', [paciente_id], one=True)

def crear_historial_clinico(paciente_id, datos):
    db = get_db()
    db.execute('''
        INSERT INTO historial_clinico (
            paciente_id, cirugias, padecimientos, medicamentos, suplementos,
            enfermedades_previas, enfermedades_actuales, tipo_actividad_fisica,
            frecuencia_actividad_fisica, tiempo_actividad_fisica,
            numero_comidas_diarias, alimentos_normales, alimentos_no_gustados
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        paciente_id, datos['cirugias'], datos['padecimientos'], datos['medicamentos'],
        datos['suplementos'], datos['enfermedades_previas'], datos['enfermedades_actuales'],
        datos['tipo_actividad_fisica'], datos['frecuencia_actividad_fisica'],
        datos['tiempo_actividad_fisica'], datos['numero_comidas_diarias'],
        datos['alimentos_normales'], datos['alimentos_no_gustados']
    ))
    db.commit()

def actualizar_historial_clinico(paciente_id, datos):
    db = get_db()
    db.execute('''
        UPDATE historial_clinico SET
            cirugias = ?, padecimientos = ?, medicamentos = ?, suplementos = ?,
            enfermedades_previas = ?, enfermedades_actuales = ?, tipo_actividad_fisica = ?,
            frecuencia_actividad_fisica = ?, tiempo_actividad_fisica = ?,
            numero_comidas_diarias = ?, alimentos_normales = ?, alimentos_no_gustados = ?
        WHERE paciente_id = ?
    ''', (
        datos['cirugias'], datos['padecimientos'], datos['medicamentos'],
        datos['suplementos'], datos['enfermedades_previas'], datos['enfermedades_actuales'],
        datos['tipo_actividad_fisica'], datos['frecuencia_actividad_fisica'],
        datos['tiempo_actividad_fisica'], datos['numero_comidas_diarias'],
        datos['alimentos_normales'], datos['alimentos_no_gustados'], paciente_id
    ))
    db.commit()

def registrar_pago(paciente_id, fecha_pago):
    db = get_db()
    db.execute('INSERT INTO pagos (paciente_id, fecha_pago) VALUES (?, ?)', (paciente_id, fecha_pago))
    db.commit()

def obtener_ultimo_pago(paciente_id):
    return query_db('SELECT fecha_pago FROM pagos WHERE paciente_id = ? ORDER BY fecha_pago DESC LIMIT 1', [paciente_id], one=True)

def actualizar_estatus_paciente(paciente_id, estatus):
    db = get_db()
    db.execute('UPDATE pacientes SET estatus = ? WHERE id = ?', (estatus, paciente_id))
    db.commit()

