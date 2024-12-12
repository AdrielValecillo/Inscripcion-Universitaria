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
    
@student_router.get("/api/students/{student_id}", tags=["Students"])
def get_student_by_id(student_id: int):
    try:
        student = student_services.get_estudiante_by_id(student_id)
        return {"status": True, "data": student, "message": "Student retrieved successfully", "status_code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "status_code": e.status_code}
    
@student_router.get("/api/students", tags=["Students"])
def get_all_students():
    try:
        students = student_services.get_all_estudiantes()
        return {"status": True, "data": students, "message": "Students retrieved successfully", "status_code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "status_code": e.status_code}