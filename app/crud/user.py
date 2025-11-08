# app/crud/user.py
from sqlalchemy.orm import Session
from app.models.user import DBUser, UserCreate
from passlib.context import CryptContext

# 1. Necesitas esta librería para hashear contraseñas
# Instálala si no lo has hecho: pip install "passlib[bcrypt]"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

# --- OPERACIONES CRUD ---

def get_user_by_email(db: Session, email: str):
    return db.query(DBUser).filter(DBUser.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DBUser).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    # Hashear la contraseña antes de guardar
    hashed_password = get_password_hash(user.password)
    
    # Crear la instancia del modelo de la DB
    db_user = DBUser(
        email=user.email,
        hashed_password=hashed_password,
        is_active=user.is_active
    )
    
    # Añadir a la sesión, hacer commit, y refrescar para obtener el ID
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
