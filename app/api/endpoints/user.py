from fastapi import APIRouter, Depends, HTTPException
from app.services.user_services import UserServices
import app.db.schemas.user_schema as schemas

user_router = APIRouter()
user_services = UserServices()

@user_router.post("/api/users", tags=["users"])
def create_user(user: schemas.UserBase):
    try:
        user = user_services.create_user(user)
        return {"status": True, "data": user, "message": "User created successfully", "status_code": 201}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "status_code": e.status_code}    
    
@user_router.get("/api/users", tags=["users"])
def get_all_users():
    try:
        users = user_services.get_all_users()
        return {"status": True, "data": users, "message": "Users retrieved successfully", "status_code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "status_code": e.status_code}

@user_router.get("/api/users/{user_id}", tags=["users"])
def get_user_by_id(user_id: int):
    try:
        user = user_services.get_user_by_id(user_id)
        return {"status": True, "data": user, "message": "User retrieved successfully", "status_code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "status_code": e.status_code}
    
@user_router.put("/api/users/{user_id}", tags=["users"])
def update_user(user_id: int, user: schemas.UserBase):
    try:
        user = user_services.update_user(user_id, user)
        return {"status": True, "data": user, "message": "User updated successfully", "status_code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "status_code": e.status_code}
    
@user_router.get("/api/users/cedula/{cedula}", tags=["users"])
def get_user_by_cedula(cedula: str):
    try:
        user = user_services.get_user_by_cedula(cedula)
        return {"status": True, "data": user, "message": "User retrieved successfully", "status_code": 200}
    except HTTPException as e:
        return {"status": False, "data": None, "message": e.detail, "status_code": e.status_code}
    