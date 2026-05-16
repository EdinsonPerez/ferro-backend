from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.clase import Clase
from app.models.deporte import Deporte
from app.models.profesor import Profesor

router = APIRouter(prefix="/clases", tags=["Clases"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def crear_clase(
    deporte_id: int,
    profesor_id: int,
    dia: str,
    horario: str,
    db: Session = Depends(get_db)
):

    deporte = db.query(Deporte).filter(Deporte.id == deporte_id).first()
    profesor = db.query(Profesor).filter(Profesor.id == profesor_id).first()

    if not deporte:
        raise HTTPException(status_code=404, detail="Deporte no encontrado")

    if not profesor:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")

    clase = Clase(
        deporte_id=deporte_id,
        profesor_id=profesor_id,
        dia=dia,
        horario=horario
    )

    db.add(clase)
    db.commit()
    db.refresh(clase)

    return clase


@router.get("/")
def listar_clases(db: Session = Depends(get_db)):
    return db.query(Clase).all()