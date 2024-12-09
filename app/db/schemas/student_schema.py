from pydantic import BaseModel, Field


class StudentBase(BaseModel):
    telefono: str = Field(..., max_length=10)
    direccion: str = Field(..., max_length=100)



class EstudentCreate(StudentBase):
    id_estudiante: int

    class Config:
        from_attributes = True