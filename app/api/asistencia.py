from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.asistencia_service import registrar_asistencia

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