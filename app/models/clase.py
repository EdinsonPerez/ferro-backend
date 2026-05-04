from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Clase(Base):
    __tablename__ = "clases"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    dia = Column(String(50))