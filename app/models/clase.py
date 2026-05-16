from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Clase(Base):
    __tablename__ = "clases"

    id = Column(Integer, primary_key=True, index=True)

    deporte_id = Column(Integer, ForeignKey("deportes.id"))
    profesor_id = Column(Integer, ForeignKey("profesores.id"))

    dia = Column(String(50))        # Ej: Lunes
    horario = Column(String(50))    # Ej: 18:00 - 19:00

    deporte = relationship("Deporte")
    profesor = relationship("Profesor")