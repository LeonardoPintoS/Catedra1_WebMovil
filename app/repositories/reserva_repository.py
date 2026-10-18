from sqlalchemy.orm import Session
from app.models import Reserva
from typing import Optional

class ReservaRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, usuario_id: Optional[int] = None, espacio_id: Optional[int] = None, fecha: Optional[str] = None, estado: Optional[str] = None, skip: int = 0, limit: int = 10):
        query = self.db.query(Reserva)
        if usuario_id is not None:
            query = query.filter(Reserva.id_usuario == usuario_id)
        if espacio_id is not None:
            query = query.filter(Reserva.id_espacio == espacio_id)
        if fecha is not None:
            query = query.filter(Reserva.fecha == fecha)
        if estado is not None:
            query = query.filter(Reserva.estado == estado)
        return query.offset(skip).limit(limit).all()

    def get_by_id(self, reserva_id: int):
        return self.db.query(Reserva).filter(Reserva.id == reserva_id).first()

    def get_overlapping_reservations(self, id_espacio: int, fecha: str, hora_inicio: str, hora_fin: str):
        return self.db.query(Reserva).filter(
            Reserva.id_espacio == id_espacio,
            Reserva.fecha == fecha,
            Reserva.estado == "activa",
            Reserva.hora_inicio < hora_fin,
            Reserva.hora_fin > hora_inicio
        ).all()

    def create(self, data: dict):
        reserva = Reserva(**data)
        self.db.add(reserva)
        self.db.commit()
        self.db.refresh(reserva)
        return reserva

    def update(self, reserva: Reserva, data: dict):
        for key, value in data.items():
            setattr(reserva, key, value)
        self.db.commit()
        self.db.refresh(reserva)
        return reserva

    def delete(self, reserva: Reserva):
        self.db.delete(reserva)
        self.db.commit()