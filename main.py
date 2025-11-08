# main.py
from fastapi import FastAPI
from app.routers import user as user_router # Importamos el router desde la nueva ubicación

app = FastAPI(title="Mi Backend FastAPI")

# Incluye el router de usuarios
app.include_router(user_router.router)

@app.get("/")
def read_root():
    return {"message": "¡Servidor de FastAPI activo!"}
