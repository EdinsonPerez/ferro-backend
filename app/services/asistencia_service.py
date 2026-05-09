from sqlalchemy.orm import Session

from app.models.asistencia import Asistencia
from app.models.alumno import Alumno
from app.models.estado_alumno import EstadoAlumno


def registrar_asistencia(db: Session, alumno_id: int, clase_id: int, presente: bool):

    asistencia = Asistencia(
        alumno_id=alumno_id,
        clase_id=clase_id,
        presente=presente
    )

    db.add(asistencia)
    db.commit()
    db.refresh(asistencia)

    # LÓGICA BPMN
    if not presente:
        ausencias = db.query(Asistencia).filter(
            Asistencia.alumno_id == alumno_id,
            Asistencia.presente == False
        ).count()

        if ausencias >= 3:
            estado = db.query(EstadoAlumno).filter_by(codigo="EN_SEGUIMIENTO").first()
            alumno = db.query(Alumno).filter(Alumno.id == alumno_id).first()

            if estado and alumno:
                alumno.estado_id = estado.id
                db.commit()

    return asistencia