from pydantic import BaseModel

class AlumnoBase(BaseModel):
    nombre: str
    apellido: str

class AlumnoCreate(AlumnoBase):
    estado_id: int

class AlumnoResponse(AlumnoBase):
    id: int
    estado_id: int

    class Config:
        orm_mode = True