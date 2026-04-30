from sqlalchemy import Column, Integer, String
from app.db.base import Base

class EstadoAlumno(Base):
    __tablename__ = "estados_alumno"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(100), nullable=False)