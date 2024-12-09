import bcrypt
from app.services.base import Base
from app.db.models.models import Usuario
from fastapi import HTTPException
from app.db.schemas.user_schema import UserBase


class UserServices(Base):
    def create_user(self, user_data: dict):
        user_exist = self.get_user_by_cedula(user_data.cedula)

        if user_exist:
            raise HTTPException(status_code=400, detail="User already exist, cedula is already registered")
        
        
        user = Usuario(**user_data.dict())
        user.contraseña = bcrypt.hashpw(user.contraseña.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_cedula(self, cedula: str):
        user = self.db.query(Usuario).filter(Usuario.cedula == cedula).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    
    def get_user_by_email(self, email: str):
        user = self.db.query(Usuario).filter(Usuario.correo == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    
    def get_user_by_id(self, user_id: int):
        user = self.db.query(Usuario).filter(Usuario.id_usuario == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    
    def get_all_users(self):
        users = self.db.query(Usuario).all()
        return users
    
    def update_user(self, user_id: int, user_data: dict):
        user = self.get_user_by_id(user_id)
        user.nombre = user_data.nombre
        user.correo = user_data.correo
        user.rol = user_data.rol
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def delete_user(self, user_id: int):
        user = self.get_user_by_id(user_id)
        self.db.delete(user)
        self.db.commit()
        self.db.refresh(user)
        return user