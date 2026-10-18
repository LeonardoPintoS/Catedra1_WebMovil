from fastapi import HTTPException, status
from app.repositories.reserva_repository import ReservaRepository
from app.repositories.espacio_repository import EspacioRepository
from app.repositories.usuario_repository import UsuarioRepository

class ReservaService:
    def __init__(self, db):
        self.reserva_repo = ReservaRepository(db)
        self.espacio_repo = EspacioRepository(db)
        self.usuario_repo = UsuarioRepository(db)

    def crear_reserva(self, data_in):
        if not self.usuario_repo.get_by_id(data_in.id_usuario):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario inexistente")

        if not self.espacio_repo.get_by_id(data_in.id_espacio):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Espacio inexistente")

        superpuestas = self.reserva_repo.get_overlapping_reservations(
            data_in.id_espacio, data_in.fecha, data_in.hora_inicio, data_in.hora_fin
        )
        if superpuestas:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
                detail="El espacio se encuentra ocupado en ese rango de horario"
            )

        if data_in.hora_inicio >= data_in.hora_fin:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
                detail="La hora de inicio debe ser anterior a la hora de fin"
            )

        return self.reserva_repo.create(data_in.model_dump())