from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.models.alumno_tutor import alumno_tutor  # tabla intermedia

class Tutor(Base):
    __tablename__ = "tutores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)

    alumnos = relationship(
        "Alumno",
        secondary=alumno_tutor,
        back_populates="tutores"
    )