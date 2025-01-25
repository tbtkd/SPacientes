-- Verificar si la tabla pacientes existe
CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido_paterno TEXT NOT NULL,
    apellido_materno TEXT NOT NULL,
    fecha_nacimiento TEXT NOT NULL,
    telefono TEXT NOT NULL,
    correo TEXT UNIQUE NOT NULL,
    ciudad TEXT NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estatus TEXT CHECK(estatus IN ('activo', 'cancelado', 'baja')) DEFAULT 'activo'
);

-- Verificar si la tabla historial_clinico existe
CREATE TABLE IF NOT EXISTS historial_clinico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER NOT NULL,
    cirugias TEXT,
    padecimientos TEXT,
    medicamentos TEXT,
    suplementos TEXT,
    enfermedades_previas TEXT,
    enfermedades_actuales TEXT,
    tipo_actividad_fisica TEXT,
    frecuencia_actividad_fisica TEXT,
    tiempo_actividad_fisica TEXT,
    numero_comidas_diarias INTEGER,
    alimentos_normales TEXT,
    alimentos_no_gustados TEXT,
    FOREIGN KEY (paciente_id) REFERENCES pacientes (id)
);

-- Verificar si la tabla pagos existe
CREATE TABLE IF NOT EXISTS pagos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paciente_id INTEGER NOT NULL,
    fecha_pago DATE NOT NULL,
    FOREIGN KEY (paciente_id) REFERENCES pacientes (id)
);

