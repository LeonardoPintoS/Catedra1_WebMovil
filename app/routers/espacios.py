from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.schemas import EspacioCreate, EspacioUpdate, EspacioResponse
from app.repositories.espacio_repository import EspacioRepository

router = APIRouter(prefix="/api/espacios", tags=["Espacios"])

@router.get("/", response_model=List[EspacioResponse])
def listar_espacios(
    capacidad: Optional[int] = Query(None, description="Filtrar capacidad mínima"),
    disponible: Optional[bool] = Query(None, description="Filtrar por disponibilidad"),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db)
):
    repo = EspacioRepository(db)
    return repo.get_all(capacidad=capacidad, disponible=disponible, skip=skip, limit=limit)

@router.get("/{id}", response_model=EspacioResponse)
def obtener_espacio(id: int, db: Session = Depends(get_db)):
    repo = EspacioRepository(db)
    espacio = repo.get_by_id(id)
    if not espacio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Espacio inexistente")
    return espacio

@router.post("/", response_model=EspacioResponse, status_code=status.HTTP_201_CREATED)
def crear_espacio(espacio_in: EspacioCreate, db: Session = Depends(get_db)):
    repo = EspacioRepository(db)
    return repo.create(espacio_in.model_dump())

@router.put("/{id}", response_model=EspacioResponse)
def actualizar_espacio(id: int, espacio_in: EspacioUpdate, db: Session = Depends(get_db)):
    repo = EspacioRepository(db)
    espacio = repo.get_by_id(id)
    if not espacio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Espacio inexistente")
    return repo.update(espacio, espacio_in.model_dump(exclude_unset=True))

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def eliminar_espacio(id: int, db: Session = Depends(get_db)):
    repo = EspacioRepository(db)
    espacio = repo.get_by_id(id)
    if not espacio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Espacio inexistente")
    repo.delete(espacio)
    return {"mensaje": "Espacio eliminado"}