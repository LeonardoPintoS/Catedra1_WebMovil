from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, index=True, nullable=False)

    reservas = relationship("Reserva", back_populates="usuario", cascade="all, delete-orphan")

class Espacio(Base):
    __tablename__ = "espacios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    ubicacion = Column(String, nullable=False)
    capacidad = Column(Integer, nullable=False)
    disponibilidad_total = Column(Boolean, default=True, nullable=False)

    reservas = relationship("Reserva", back_populates="espacio", cascade="all, delete-orphan")

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    id_espacio = Column(Integer, ForeignKey("espacios.id"), nullable=False)
    fecha = Column(String, nullable=False)
    hora_inicio = Column(String, nullable=False)
    hora_fin = Column(String, nullable=False)
    estado = Column(String, default="activa", nullable=False)

    usuario = relationship("Usuario", back_populates="reservas")
    espacio = relationship("Espacio", back_populates="reservas")