from app.db import get_db, query_db

class ValoracionAntropometrica:
    @staticmethod
    def crear(paciente_id, datos):
        db = get_db()
        try:
            db.execute('''
                INSERT INTO valoracion_antropometrica (
                    paciente_id, numero_cita, fecha, estatura, peso, imc, grasa,
                    cintura, torax, brazo, cadera, pierna, pantorrilla,
                    bicep, tricep, suprailiaco, subescapular, femoral, porcentaje_grasa
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                paciente_id, datos['numero_cita'], datos['fecha'], datos['estatura'],
                datos['peso'], datos['imc'], datos['grasa'], datos['cintura'],
                datos['torax'], datos['brazo'], datos['cadera'], datos['pierna'],
                datos['pantorrilla'], datos['bicep'], datos['tricep'],
                datos['suprailiaco'], datos['subescapular'], datos['femoral'],
                datos['porcentaje_grasa']
            ))
            db.commit()
            return True, "Valoración antropométrica registrada correctamente."
        except Exception as e:
            db.rollback()
            return False, f"Error al registrar la valoración antropométrica: {str(e)}"

    @staticmethod
    def obtener_por_paciente(paciente_id):
        return query_db('''
            SELECT * FROM valoracion_antropometrica
            WHERE paciente_id = ?
            ORDER BY fecha DESC
        ''', [paciente_id])

    @staticmethod
    def obtener_ultima_valoracion(paciente_id):
        return query_db('''
            SELECT * FROM valoracion_antropometrica
            WHERE paciente_id = ?
            ORDER BY fecha DESC
            LIMIT 1
        ''', [paciente_id], one=True)

    @staticmethod
    def obtener_todas():
        return query_db('''
            SELECT va.*, p.nombre, p.apellido_paterno, p.apellido_materno
            FROM valoracion_antropometrica va
            JOIN pacientes p ON va.paciente_id = p.id
            ORDER BY va.fecha DESC
        ''')

