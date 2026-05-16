from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Profesor(Base):
    __tablename__ = "profesores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)

    deporte_id = Column(Integer, ForeignKey("deportes.id"))

    deporte = relationship("Deporte")