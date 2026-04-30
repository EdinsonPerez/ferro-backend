from app.db.session import SessionLocal
from app.models.estado_alumno import EstadoAlumno

def seed_estados():
    db = SessionLocal()

    estados = [
        {"codigo": "ACTIVO", "descripcion": "Alumno activo"},
        {"codigo": "EN_SEGUIMIENTO", "descripcion": "Ausencias detectadas"},
        {"codigo": "BAJA_PENDIENTE", "descripcion": "Pendiente de baja"},
        {"codigo": "BAJA_CONFIRMADA", "descripcion": "Baja confirmada"}
    ]

    for estado in estados:
        existe = db.query(EstadoAlumno).filter_by(codigo=estado["codigo"]).first()
        if not existe:
            nuevo = EstadoAlumno(**estado)
            db.add(nuevo)

    db.commit()
    db.close()


if __name__ == "__main__":
    seed_estados()
    print("✅ Estados cargados correctamente")