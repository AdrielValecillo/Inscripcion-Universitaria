from fastapi import APIRouter, Depends, HTTPException
from app.services.preferencia_services import PreferenciaServices
import app.db.schemas.preferencia_schema as schemas

preferencia_router = APIRouter()
preferencia_services = PreferenciaServices()

@preferencia_router.post("/api/preferencias", tags=["Preferencias Academicas"])
def create_preferencia(preferencia: schemas.PreferenciaBase):
    try:
        preferencia = preferencia_services.create_preferencia(preferencia)
        return {"status": True, "data": preferencia, "message": "Preferencia creada exitosamente", "status_code": 201}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "status_code": e.status_code}
    
@preferencia_router.get("/api/preferencias", tags=["Preferencias Academicas"])
def get_all_preferencias():
    try:
        preferencias = preferencia_services.get_all_preferencias()
        return {"status": True, "data": preferencias, "message": "Preferencias recuperadas exitosamente", "status_code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "status_code": e.status_code}
    
@preferencia_router.get("/api/preferencias/{preferencia_id}", tags=["Preferencias Academicas"])
def get_preferencia_by_id(preferencia_id: int):
    try:
        preferencia = preferencia_services.get_preferencia_by_id(preferencia_id)
        return {"status": True, "data": preferencia, "message": "Preferencia recuperada exitosamente", "status_code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "status_code": e.status_code}