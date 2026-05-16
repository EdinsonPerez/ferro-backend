from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.alumno_tutor import alumno_tutor

class Alumno(Base):
    __tablename__ = "alumnos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    estado_id = Column(Integer, ForeignKey("estados_alumno.id"), nullable=False)
    alerta_enviada = Column(Boolean, default=False)

    # Relacion simple
    estado = relationship("EstadoAlumno")

    # Relación mucho a mucho
    tutores = relationship(
        "Tutor",
        secondary=alumno_tutor,
        back_populates="alumnos"
    )
    