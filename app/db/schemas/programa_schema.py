from pydantic import BaseModel, Field

class ProgramaBase(BaseModel):
    nombre_programa: str = Field(..., max_length=100)
    descripcion: str = Field(..., max_length=200)

class ProgramaCreate(ProgramaBase):
    id_programa: int

    class Config:
        from_attributes = True