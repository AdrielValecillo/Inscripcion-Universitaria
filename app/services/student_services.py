from app.services.base import Base
from app.db.models.models import Estudiante
from fastapi import HTTPException
from app.services.user_services import UserServices
from datetime import datetime
from sqlalchemy.orm import joinedload

user_services = UserServices()

class EstudianteServices(Base):
    def create_estudiante(self, estudiante_data: dict, cedula: str):
        user = user_services.get_user_by_cedula(cedula)

        if not user:
            raise HTTPException(status_code=404, detail="User not found, cedula not registered")

        estudiante = Estudiante(**estudiante_data.dict())
        estudiante.id_estudiante = user.id_usuario
        estudiante.fecha_registro = datetime.now()
        estudiante.estado = "activo"
        self.db.add(estudiante)
        self.db.commit()
        self.db.refresh(estudiante)
        return estudiante
    
    def get_estudiante_by_id(self, estudiante_id: int):
        estudiante = self.db.query(Estudiante).options(joinedload(Estudiante.usuario)).filter(Estudiante.id_estudiante == estudiante_id).first()
        if not estudiante:
            raise HTTPException(status_code=404, detail="Estudiante not found")
        return estudiante
    
    def get_all_estudiantes(self):
        estudiantes = self.db.query(Estudiante).options(joinedload(Estudiante.usuario)).all()
        return estudiantes
    
