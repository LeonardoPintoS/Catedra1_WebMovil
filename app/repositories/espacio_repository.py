from sqlalchemy.orm import Session
from app.models import Espacio
from typing import Optional

class EspacioRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, capacidad: Optional[int] = None, disponible: Optional[bool] = None, skip: int = 0, limit: int = 10):
        query = self.db.query(Espacio)
        if capacidad is not None:
            query = query.filter(Espacio.capacidad >= capacidad)
        if disponible is not None:
            query = query.filter(Espacio.disponibilidad_total == disponible)
        return query.offset(skip).limit(limit).all()

    def get_by_id(self, espacio_id: int):
        return self.db.query(Espacio).filter(Espacio.id == espacio_id).first()

    def create(self, data: dict):
        espacio = Espacio(**data)
        self.db.add(espacio)
        self.db.commit()
        self.db.refresh(espacio)
        return espacio

    def update(self, espacio: Espacio, data: dict):
        for key, value in data.items():
            setattr(espacio, key, value)
        self.db.commit()
        self.db.refresh(espacio)
        return espacio

    def delete(self, espacio: Espacio):
        self.db.delete(espacio)
        self.db.commit()