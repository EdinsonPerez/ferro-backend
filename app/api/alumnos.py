from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.alumno import AlumnoCreate, AlumnoResponse
from app.services.alumno_service import crear_alumno
from app.models.alumno import Alumno

router = APIRouter(prefix="/alumnos", tags=["Alumnos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AlumnoResponse)
def create_alumno(alumno: AlumnoCreate, db: Session = Depends(get_db)):
    return crear_alumno(db, alumno)

@router.get("/", response_model=list[AlumnoResponse])
def get_alumnos(db: Session = Depends(get_db)):
    return db.query(Alumno).all()

@router.get("/en-seguimiento")
def alumnos_en_seguimiento(db: Session = Depends(get_db)):
    from app.models.estado_alumno import EstadoAlumno

    estado = db.query(EstadoAlumno).filter_by(codigo="EN_SEGUIMIENTO").first()

    return db.query(Alumno).filter(Alumno.estado_id == estado.id).all()

@router.get("/{alumno_id}/tutores")
def obtener_tutores_alumno(alumno_id: int, db: Session = Depends(get_db)):

    alumno = db.query(Alumno).filter(Alumno.id == alumno_id).first()

    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")

    return alumno.tutores

@router.get("/{alumno_id}", response_model=AlumnoResponse)
def get_alumno(alumno_id: int, db: Session = Depends(get_db)):
    alumno = db.query(Alumno).filter(Alumno.id == alumno_id).first()

    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")

    return alumno

@router.delete("/{alumno_id}")
def delete_alumno(alumno_id: int, db: Session = Depends(get_db)):
    alumno = db.query(Alumno).filter(Alumno.id == alumno_id).first()

    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")

    db.delete(alumno)
    db.commit()

    return {"message": "Alumno eliminado"}