from fastapi import APIRouter, Depends, HTTPException
from app.services.programas_services import ProgramaServices
import app.db.schemas.programa_schema as schemas

programa_router = APIRouter()
programa_services = ProgramaServices()

@programa_router.post("/api/programas", tags=["Programas Academicos"])
def create_programa(programa: schemas.ProgramaBase):
    try:
        programa = programa_services.create_programa(programa)
        return {"status": True, "data": programa, "message": "Programa creado exitosamente", "status_code": 201}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "status_code": e.status_code}
    
@programa_router.get("/api/programas", tags=["Programas Academicos"])
def get_all_programas():
    try:
        programas = programa_services.get_all_programas()
        return {"status": True, "data": programas, "message": "Programas recuperados exitosamente", "status_code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "status_code": e.status_code}
    
@programa_router.get("/api/programas/{programa_id}", tags=["Programas Academicos"])
def get_programa_by_id(programa_id: int):
    try:
        programa = programa_services.get_programa_by_id(programa_id)
        return {"status": True, "data": programa, "message": "Programa recuperado exitosamente", "status_code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "status_code": e.status_code}
    
@programa_router.put("/api/programas/{programa_id}", tags=["Programas Academicos"])
def update_programa(programa_id: int, programa: schemas.ProgramaBase):
    try:
        programa = programa_services.update_programa(programa_id, programa)
        return {"status": True, "data": programa, "message": "Programa actualizado exitosamente", "status_code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "status_code": e.status_code}
    
@programa_router.delete("/api/programas/{programa_id}", tags=["Programas Academicos"])
def delete_programa(programa_id: int):
    try:
        programa = programa_services.delete_programa(programa_id)
        return {"status": True, "data": programa, "message": "Programa eliminado exitosamente", "status_code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "status_code": e.status_code}