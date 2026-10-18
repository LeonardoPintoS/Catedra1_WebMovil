from sqlalchemy.orm import Session
from app.models import Usuario

class UsuarioRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 10):
        return self.db.query(Usuario).offset(skip).limit(limit).all()

    def get_by_id(self, usuario_id: int):
        return self.db.query(Usuario).filter(Usuario.id == usuario_id).first()

    def create(self, data: dict):
        usuario = Usuario(**data)
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def update(self, usuario: Usuario, data: dict):
        for key, value in data.items():
            setattr(usuario, key, value)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def delete(self, usuario: Usuario):
        self.db.delete(usuario)
        self.db.commit()