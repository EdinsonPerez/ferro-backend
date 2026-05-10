from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class Alumno(Base):
    __tablename__ = "alumnos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    estado_id = Column(Integer, ForeignKey("estados_alumno.id"), nullable=False)
    alerta_enviada = Column(Boolean, default=False)

    estado = relationship("EstadoAlumno")

    