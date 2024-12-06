from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    cedula: str
    nombre: str
    correo: EmailStr
    contraseña: str
    rol: str

class UserCreate(UserBase):
    id_usuario: int

    class Config:
        orm_mode = True


