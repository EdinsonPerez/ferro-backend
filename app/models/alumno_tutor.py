from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.base import Base

alumno_tutor = Table(
    "alumno_tutor",
    Base.metadata,
    Column("alumno_id", Integer, ForeignKey("alumnos.id")),
    Column("tutor_id", Integer, ForeignKey("tutores.id"))
)