from sqlalchemy.orm import Session

from app.models.alumno import Alumno
from app.models.estado_alumno import EstadoAlumno
from app.schemas.alumno import AlumnoCreate


def crear_alumno(db: Session, alumno_in: AlumnoCreate):
    estado = db.query(EstadoAlumno).filter_by(codigo="ACTIVO").first()

    if not estado:
        raise Exception("No existe el esatdo ACTIVO. Ejecutar seed.")

    alumno = Alumno(
        nombre=alumno_in.nombre,
        apellido=alumno_in.apellido,
        estado_id=estado.id
    )

    db.add(alumno)
    db.commit()
    db.refresh(alumno)

    return alumno