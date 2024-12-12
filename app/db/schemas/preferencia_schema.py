from pydantic import BaseModel, Field


class PreferenciaBase(BaseModel):
    id_estudiante: int = Field(..., alias="id_estudiante")
    id_programa_principal: int = Field(..., alias="id_programa_principal")
    id_programa_secundario: int = Field(None, alias="id_programa_secundario")


class PreferenciaCreate(PreferenciaBase):
    id_preferencia: int

    class Config:
        from_attributes = True