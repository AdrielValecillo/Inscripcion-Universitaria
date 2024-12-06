from fastapi import FastAPI
from app.db.db_config import engine
import app.db.models.models as db_models

app = FastAPI()
app.title = "Inscripcion Universitaria"

db_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}


