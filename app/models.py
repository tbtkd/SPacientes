from app import db
from datetime import datetime

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    ciudad = db.Column(db.String(100), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'<Paciente {self.nombre} {self.apellido_paterno}>'

