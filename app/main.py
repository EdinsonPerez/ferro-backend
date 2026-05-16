from fastapi import FastAPI

from app.api.alumnos import router as alumnos_router
from app.api.asistencia import router as asistencia_router
from app.api.deporte import router as deporte_router
from app.api.profesor import router as profesor_router
from app.api.clase import router as clase_router
from app.api.tutor import router as tutor_router
from app.db.base import Base
from app.db.session import engine

# 👇 IMPORTAMOS REGISTRY (esto registra modelos SIN romper imports)
from app.db import models_registry

app = FastAPI(title="Sistema Deportivo Ferro")

Base.metadata.create_all(bind=engine)

app.include_router(alumnos_router)
app.include_router(asistencia_router)
app.include_router(deporte_router)
app.include_router(profesor_router)
app.include_router(clase_router)
app.include_router(tutor_router)

@app.get("/health")
def health():
    return {"status": "ok"}

