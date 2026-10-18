from fastapi import FastAPI
from app.middleware import add_process_time_header
from app.routers import usuarios, espacios, reservas

app = FastAPI(
    title="API de Gestión de Espacios",
    description="Backend modular con FastAPI, Patrón Repository y Principios SOLID.",
    version="1.0.0"
)

app.middleware("http")(add_process_time_header)

app.include_router(usuarios.router)
app.include_router(espacios.router)
app.include_router(reservas.router)

@app.get("/", tags=["Root"])
def root():
    return {"mensaje": "Bienvenido a la API de Gestión de Espacios"}