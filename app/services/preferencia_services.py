from app.services.base import Base
from app.db.models.models import PreferenciaAcademica, Estudiante
from fastapi import HTTPException
from sqlalchemy.orm import joinedload



class PreferenciaServices(Base):
    def create_preferencia(self, preferencia_data: dict):
        preferencia_exist = self.db.query(PreferenciaAcademica).filter(PreferenciaAcademica.id_estudiante == preferencia_data.id_estudiante).first()

        if preferencia_exist:
            raise HTTPException(status_code=400, detail="Preferencia already exist, student is already registered")
     
        preferencia = PreferenciaAcademica(**preferencia_data.dict())
        self.db.add(preferencia)
        self.db.commit()
        self.db.refresh(preferencia)
        return preferencia
    
    
    def get_all_preferencias(self):
        preferencias = self.db.query(PreferenciaAcademica).options(
            joinedload(PreferenciaAcademica.estudiante).joinedload(Estudiante.usuario),
            joinedload(PreferenciaAcademica.programa_principal),
            joinedload(PreferenciaAcademica.programa_secundario)
        ).all()
        return preferencias

    def get_preferencia_by_id(self, preferencia_id: int):
        preferencia = self.db.query(PreferenciaAcademica).options(
            joinedload(PreferenciaAcademica.estudiante).joinedload(Estudiante.usuario),
            joinedload(PreferenciaAcademica.programa_principal),
            joinedload(PreferenciaAcademica.programa_secundario)
        ).filter(PreferenciaAcademica.id_preferencia == preferencia_id).first()
        if not preferencia:
            raise HTTPException(status_code=404, detail="Preferencia not found")
        return preferencia