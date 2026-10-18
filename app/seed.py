from app.database import SessionLocal
from app.models import Usuario, Espacio, Reserva

def poblar_base_datos():
    db = SessionLocal()
    
    if db.query(Usuario.id).first():
        print("La base de datos ya contiene datos.")
        db.close()
        return

    print("Cargando datos iniciales...")

    # 5 Usuarios
    usuarios = [
        Usuario(nombre="Leonardo Pinto", correo="leonardo.pinto@alumnos.ucn.cl"),
        Usuario(nombre="Ana Gómez", correo="ana.gomez@ucn.cl"),
        Usuario(nombre="Carlos Ruiz", correo="carlos.ruiz@ucn.cl"),
        Usuario(nombre="María Silva", correo="maria.silva@ucn.cl"),
        Usuario(nombre="Pedro Soto", correo="pedro.soto@ucn.cl"),
    ]
    db.add_all(usuarios)
    db.commit()

    # 10 Espacios
    espacios = [
        Espacio(nombre=f"Sala de Reuniones {i}", ubicacion=f"Piso {i}", capacidad=i * 5, disponibilidad_total=True)
        for i in range(1, 11)
    ]
    db.add_all(espacios)
    db.commit()

    # 15 Reservas
    reservas = []
    for i in range(1, 16):
        id_usuario = (i % 5) + 1
        id_espacio = (i % 10) + 1
        reservas.append(
            Reserva(
                id_usuario=id_usuario,
                id_espacio=id_espacio,
                fecha="2026-11-01",
                hora_inicio=f"{8 + (i % 10):02d}:00",
                hora_fin=f"{9 + (i % 10):02d}:00",
                estado="activa"
            )
        )
    
    db.add_all(reservas)
    db.commit()
    db.close()
    print("¡Datos iniciales cargados con éxito!")

if __name__ == "__main__":
    poblar_base_datos()