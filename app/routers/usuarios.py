from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from app.repositories.usuario_repository import UsuarioRepository

router = APIRouter(prefix="/api/usuarios", tags=["Usuarios"])

@router.get("/", response_model=List[UsuarioResponse])
def listar_usuarios(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=50), db: Session = Depends(get_db)):
    repo = UsuarioRepository(db)
    return repo.get_all(skip=skip, limit=limit)

@router.get("/{id}", response_model=UsuarioResponse)
def obtener_usuario(id: int, db: Session = Depends(get_db)):
    repo = UsuarioRepository(db)
    usuario = repo.get_by_id(id)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario inexistente")
    return usuario

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def crear_usuario(usuario_in: UsuarioCreate, db: Session = Depends(get_db)):
    repo = UsuarioRepository(db)
    return repo.create(usuario_in.model_dump())

@router.put("/{id}", response_model=UsuarioResponse)
def actualizar_usuario(id: int, usuario_in: UsuarioUpdate, db: Session = Depends(get_db)):
    repo = UsuarioRepository(db)
    usuario = repo.get_by_id(id)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario inexistente")
    return repo.update(usuario, usuario_in.model_dump(exclude_unset=True))

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def eliminar_usuario(id: int, db: Session = Depends(get_db)):
    repo = UsuarioRepository(db)
    usuario = repo.get_by_id(id)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario inexistente")
    repo.delete(usuario)
    return {"mensaje": "Usuario eliminado"}