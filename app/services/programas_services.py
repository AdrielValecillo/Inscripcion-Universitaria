from app.services.base import Base
from app.db.models.models import ProgramaAcademico
from fastapi import HTTPException


class ProgramaServices(Base):
    def create_programa(self, programa_data: dict):
        programa_exist = self.db.query(ProgramaAcademico).filter(ProgramaAcademico.nombre_programa == programa_data.nombre_programa).first()

        if programa_exist:
            raise HTTPException(status_code=400, detail="Programa already exist, name is already registered")
        
        programa = ProgramaAcademico(**programa_data.dict())
        self.db.add(programa)
        self.db.commit()
        self.db.refresh(programa)
        return programa

    def get_programa_by_id(self, programa_id: int):
        programa = self.db.query(ProgramaAcademico).filter(ProgramaAcademico.id_programa == programa_id).first()
        if not programa:
            raise HTTPException(status_code=404, detail="Programa not found")
        return programa
    
    def get_all_programas(self):
        programas = self.db.query(ProgramaAcademico).all()
        return programas
    
    def update_programa(self, programa_id: int, programa_data: dict):
        programa = self.get_programa_by_id(programa_id)
        programa.nombre_programa = programa_data.nombre_programa
        self.db.commit()
        self.db.refresh(programa)
        return programa
    
    def delete_programa(self, programa_id: int):
        programa = self.get_programa_by_id(programa_id)
        self.db.delete(programa)
        self.db.commit()
        self.db.refresh(programa)

        