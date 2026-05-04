from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Asistencia(Base):
    __tablename__ = "asistencias"

    id = Column(Integer, primary_key=True)

    alumno_id = Column(Integer, ForeignKey("alumnos.id"))
    clase_id = Column(Integer, ForeignKey("clases.id"))

    presente = Column(Boolean)

    alumno = relationship("Alumno")
    clase = relationship("Clase")