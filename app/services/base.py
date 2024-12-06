from app.db.db_config import SessionLocal


class Base:
    def __init__(self):
        self.db = SessionLocal()