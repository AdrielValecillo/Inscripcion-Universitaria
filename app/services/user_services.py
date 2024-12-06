import bcrypt
from app.services.base import Base
from app.db.models.models import Usuario
from fastapi import HTTPException


class UserServices(Base):
    def create_user(self, user_data: dict):
        user = Usuario(**user_data)
        user.contraseña = bcrypt.hashpw(user.contraseña.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_email(self, email: str):
        user = self.db.query(Usuario).filter(Usuario.correo == email).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def get_user_by_id(self, user_id: int):
        user = self.db.query(Usuario).filter(Usuario.id_usuario == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def verify_password(self, plain_password: str, hashed_password: str):
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))