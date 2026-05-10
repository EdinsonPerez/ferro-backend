from datetime import date, timedelta
from sqlalchemy.orm import Session
from app.models.asistencia import Asistencia
from app.models.alumno import Alumno
from app.models.estado_alumno import EstadoAlumno

def obtener_ausencias_ultimos_7_dias(db: Session, alumno_id: int):
    hoy = date.today()
    hace_7_dias = hoy - timedelta(days=7)

    ausencias = db.query(Asistencia).filter(
        Asistencia.alumno_id == alumno_id,
        Asistencia.presente == False,
        Asistencia.justificada == False,
        Asistencia.fecha >= hace_7_dias
    ).all()

    return ausencias


def registrar_asistencia(db: Session, alumno_id: int, clase_id: int, presente: bool):

    asistencia = Asistencia(
        alumno_id=alumno_id,
        clase_id=clase_id,
        presente=presente
    )

    db.add(asistencia)
    db.commit()
    db.refresh(asistencia)

    # 🔥 SOLO SI ES AUSENCIA
    if not presente:

        ausencias_recientes = obtener_ausencias_ultimos_7_dias(db, alumno_id)

        alumno = db.query(Alumno).filter(Alumno.id == alumno_id).first()

        if alumno and len(ausencias_recientes) == 3 and not alumno.alerta_enviada:
            manejar_alerta_ausencias(db, alumno_id)

            alumno.alerta_enviada = True
            db.commit()
            

    return asistencia

def manejar_alerta_ausencias(db: Session, alumno_id: int):
    print(f"Alumno {alumno_id} tiene 3 o más ausencias en los últimos 7 días")

    enviar_correo_tutor(alumno_id)

    # simulamos respuesta del tutor
    decision = "SI"  # en futuro vendrá de UI o API

    if decision == "SI":
        notificar_administracion(alumno_id)

def enviar_correo_tutor(alumno_id: int):
    print(f"Email al tutor: El alumno {alumno_id} presenta inasistencias.")
    print("¿Desea desvincular al alumno?")

def notificar_administracion(alumno_id: int):
    print(f"Email a administración:")
    print(f"Alumno {alumno_id} será dado de baja.")
    print("No generar cobro de matrícula.")