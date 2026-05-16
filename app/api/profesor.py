from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.profesor import Profesor
from app.models.deporte import Deporte

router = APIRouter(prefix="/profesores", tags=["Profesores"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def crear_profesor(nombre: str, deporte_id: int, db: Session = Depends(get_db)):

    deporte = db.query(Deporte).filter(Deporte.id == deporte_id).first()

    if not deporte:
        raise HTTPException(status_code=404, detail="Deporte no encontrado")

    profesor = Profesor(nombre=nombre, deporte_id=deporte_id)

    db.add(profesor)
    db.commit()
    db.refresh(profesor)

    return profesor


@router.get("/")
def listar_profesores(db: Session = Depends(get_db)):
    return db.query(Profesor).all()


@router.get("/{profesor_id}")
def obtener_profesor(profesor_id: int, db: Session = Depends(get_db)):
    profesor = db.query(Profesor).filter(Profesor.id == profesor_id).first()

    if not profesor:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")

    return profesor


@router.delete("/{profesor_id}")
def eliminar_profesor(profesor_id: int, db: Session = Depends(get_db)):
    profesor = db.query(Profesor).filter(Profesor.id == profesor_id).first()

    if not profesor:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")

    db.delete(profesor)
    db.commit()

    return {"message": "Profesor eliminado"}