from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.schemas import ReservaCreate, ReservaUpdate, ReservaResponse
from app.repositories.reserva_repository import ReservaRepository
from app.services.reserva_service import ReservaService

router = APIRouter(prefix="/api/reservas", tags=["Reservas"])

@router.get("/", response_model=List[ReservaResponse])
def listar_reservas(
    usuario_id: Optional[int] = Query(None, alias="usuario"),
    espacio_id: Optional[int] = Query(None, alias="espacio"),
    fecha: Optional[str] = None,
    estado: Optional[str] = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db)
):
    repo = ReservaRepository(db)
    return repo.get_all(usuario_id=usuario_id, espacio_id=espacio_id, fecha=fecha, estado=estado, skip=skip, limit=limit)

@router.get("/{id}", response_model=ReservaResponse)
def obtener_reserva(id: int, db: Session = Depends(get_db)):
    repo = ReservaRepository(db)
    reserva = repo.get_by_id(id)
    if not reserva:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reserva inexistente")
    return reserva

@router.post("/", response_model=ReservaResponse, status_code=status.HTTP_201_CREATED)
def crear_reserva(reserva_in: ReservaCreate, db: Session = Depends(get_db)):
    service = ReservaService(db)
    return service.crear_reserva(reserva_in)

@router.patch("/{id}", response_model=ReservaResponse)
def actualizar_estado_reserva(id: int, reserva_in: ReservaUpdate, db: Session = Depends(get_db)):
    repo = ReservaRepository(db)
    reserva = repo.get_by_id(id)
    if not reserva:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reserva inexistente")
    return repo.update(reserva, reserva_in.model_dump(exclude_unset=True))

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def eliminar_reserva(id: int, db: Session = Depends(get_db)):
    repo = ReservaRepository(db)
    reserva = repo.get_by_id(id)
    if not reserva:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reserva inexistente")
    repo.delete(reserva)
    return {"mensaje": "Reserva eliminada exitosamente"}