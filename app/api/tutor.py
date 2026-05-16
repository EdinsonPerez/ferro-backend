from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.tutor import Tutor
from app.models.alumno import Alumno

router = APIRouter(prefix="/tutores", tags=["Tutores"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def crear_tutor(nombre: str, email: str, db: Session = Depends(get_db)):

    tutor = Tutor(nombre=nombre, email=email)

    db.add(tutor)
    db.commit()
    db.refresh(tutor)

    return tutor


@router.get("/")
def listar_tutores(db: Session = Depends(get_db)):
    return db.query(Tutor).all()


@router.post("/asignar/")
def asignar_tutor(alumno_id: int, tutor_id: int, db: Session = Depends(get_db)):

    alumno = db.query(Alumno).filter(Alumno.id == alumno_id).first()
    tutor = db.query(Tutor).filter(Tutor.id == tutor_id).first()

    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")

    if not tutor:
        raise HTTPException(status_code=404, detail="Tutor no encontrado")

    alumno.tutores.append(tutor)
    db.commit()

    return {"message": "Tutor asignado al alumno"}