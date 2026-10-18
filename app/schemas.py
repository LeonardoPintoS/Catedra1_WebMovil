from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioCreate(BaseModel):
    nombre: str
    correo: EmailStr

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[EmailStr] = None

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    correo: str

    class Config:
        from_attributes = True

class EspacioCreate(BaseModel):
    nombre: str
    ubicacion: str
    capacidad: int
    disponibilidad_total: bool = True

class EspacioUpdate(BaseModel):
    nombre: Optional[str] = None
    ubicacion: Optional[str] = None
    capacidad: Optional[int] = None
    disponibilidad_total: Optional[bool] = None

class EspacioResponse(BaseModel):
    id: int
    nombre: str
    ubicacion: str
    capacidad: int
    disponibilidad_total: bool

    class Config:
        from_attributes = True

class ReservaCreate(BaseModel):
    id_usuario: int
    id_espacio: int
    fecha: str
    hora_inicio: str
    hora_fin: str

class ReservaUpdate(BaseModel):
    estado: Optional[str] = None
    fecha: Optional[str] = None
    hora_inicio: Optional[str] = None
    hora_fin: Optional[str] = None

class ReservaResponse(BaseModel):
    id: int
    id_usuario: int
    id_espacio: int
    fecha: str
    hora_inicio: str
    hora_fin: str
    estado: str

    class Config:
        from_attributes = True