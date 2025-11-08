# app/models/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from sqlalchemy import Column, Integer, String, Boolean # <--- Nuevo
from app.db.base import Base # <--- Nuevo (la clase base de SQLAlchemy)

# -----------------
# 1. MODELO DE LA TABLA (SQLAlchemy)
# Define la estructura de la tabla 'users'
# -----------------
class DBUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String) # Campo para almacenar la contraseña hasheada
    is_active = Column(Boolean, default=True)

# -----------------
# 2. MODELOS DE LA API (Pydantic, los que ya tenías)
# -----------------
class UserBase(BaseModel):
    email: EmailStr
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    
    class Config:
        from_attributes = True
