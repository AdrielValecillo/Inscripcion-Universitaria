from fastapi import APIRouter, Depends, HTTPException
from app.services.student_services import EstudianteServices
import app.db.schemas.student_schema as schemas

student_router = APIRouter()
student_services = EstudianteServices()

@student_router.post("/api/students/{cedula}", tags=["Students"])
def create_student(student: schemas.StudentBase, cedula: str):
    try:
        student = student_services.create_estudiante(student, cedula)
        return {"status": True, "data": student, "message": "Student created successfully", "status_code": 201}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "status_code": e.status_code}