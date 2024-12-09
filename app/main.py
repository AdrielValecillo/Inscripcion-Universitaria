from fastapi import FastAPI
from app.db.db_config import engine
import app.db.models.models as db_models
from app.api.endpoints.user import user_router
from app.api.endpoints.student import student_router

app = FastAPI()
app.title = "Inscripcion Universitaria"

db_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(user_router)
app.include_router(student_router)

