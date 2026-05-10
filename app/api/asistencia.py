from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.asistencia_service import registrar_asistencia
from app.models.asistencia import Asistencia

router = APIRouter(prefix="/asistencias", tags=["Asistencias"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def crear_asistencia(alumno_id: int, clase_id: int, presente: bool, db: Session = Depends(get_db)):
    return registrar_asistencia(db, alumno_id, clase_id, presente)

@router.get("/{alumno_id}")
def historial_asistencia(alumno_id: int, db: Session = Depends(get_db)):
    return db.query(Asistencia).filter(Asistencia.alumno_id == alumno_id).all()

@router.get("/ausencias-recientes/{alumno_id}")
def ver_ausencias_recientes(alumno_id: int, db: Session = Depends(get_db)):
    from app.services.asistencia_service import obtener_ausencias_ultimos_7_dias
    return obtener_ausencias_ultimos_7_dias(db, alumno_id)