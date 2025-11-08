# app/routers/user.py
from fastapi import APIRouter, HTTPException
from app.models.user import User, UserCreate

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Simulamos una 'base de datos' con un diccionario simple
fake_db = {}
user_id_counter = 0

# Endpoint para crear un usuario
@router.post("/", response_model=User, status_code=201)
def create_new_user(user: UserCreate):
    global user_id_counter
    # Simulación de la creación en DB
    user_id_counter += 1
    new_user = User(id=user_id_counter, **user.dict(exclude={'password'}))
    fake_db[user_id_counter] = new_user.dict()
    
    return new_user

# Endpoint para obtener todos los usuarios
@router.get("/", response_model=list[User])
def read_all_users():
    return list(fake_db.values())
