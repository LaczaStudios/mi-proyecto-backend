# app/crud/user.py
from sqlalchemy.orm import Session
from app.models.user import DBUser, UserCreate
from passlib.context import CryptContext

# Configuración de hashing de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    """Genera el hash de una contraseña."""
    return pwd_context.hash(password)

# --- OPERACIONES CRUD ---

def get_user_by_email(db: Session, email: str):
    """Busca un usuario por su email."""
    return db.query(DBUser).filter(DBUser.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    """Obtiene una lista de usuarios con paginación."""
    return db.query(DBUser).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    """Crea un nuevo usuario en la base de datos."""
    hashed_password = get_password_hash(user.password)
    
    db_user = DBUser(
        email=user.email,
        hashed_password=hashed_password,
        is_active=user.is_active
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
