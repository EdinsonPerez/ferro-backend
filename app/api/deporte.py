from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.deporte import Deporte
from fastapi import HTTPException

router = APIRouter(prefix="/deportes", tags=["Deportes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def crear_deporte(nombre: str, db: Session = Depends(get_db)):
    deporte = Deporte(nombre=nombre)
    db.add(deporte)
    db.commit()
    db.refresh(deporte)
    return deporte

@router.get("/")
def listar_deportes(db: Session = Depends(get_db)):
    return db.query(Deporte).all()

@router.delete("/{deporte_id}")
def delete_deporte(deporte_id: int, db: Session = Depends(get_db)):

    deporte = db.query(Deporte).filter(Deporte.id == deporte_id).first()

    if not deporte:
        raise HTTPException(status_code=404, detail="Deporte no encontrado")

    db.delete(deporte)
    db.commit()

    return {"message": "Deporte eliminado correctamente"}