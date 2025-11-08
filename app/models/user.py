# app/models/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional

# Base para compartir atributos (ej: GET)
class UserBase(BaseModel):
    email: EmailStr
    is_active: Optional[bool] = True

# Esquema para crear un usuario (POST)
class UserCreate(UserBase):
    password: str # El password solo es necesario al crear

# Esquema completo de un usuario (incluye el ID generado por la DB)
class User(UserBase):
    id: int
    
    # Configuración opcional para trabajar con ORMs como SQLAlchemy
    class Config:
        from_attributes = True
