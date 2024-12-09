from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    cedula: str = Field(..., max_length=10)
    nombre: str = Field(..., max_length=50)
    correo: EmailStr
    contraseña: str
    rol: str 

class UserCreate(UserBase):
    pass

    class Config:
        from_attributes = True


