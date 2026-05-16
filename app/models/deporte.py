from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Deporte(Base):
    __tablename__ = "deportes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False)