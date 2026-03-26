import asyncio
from models.habitacion import Suite, Master, SuitePresidencial
from models.hotel import Hotel
from contexts_manager import GestorReservacion


async def main():
    # Crear hotel
    hotel = Hotel("Camino Real")

    # Agregar habitaciones
    hotel.agregar_habitacion(Suite(101, 1))
    hotel.agregar_habitacion(Master(102, 2))
    hotel.agregar_habitacion(Suite(103, 1))
    hotel.agregar_habitacion(SuitePresidencial(104, 3))
    hotel.agregar_habitacion(Suite(105, 1))
    hotel.agregar_habitacion(Master(106, 2))
    hotel.agregar_habitacion(Suite(107, 1))
    hotel.agregar_habitacion(SuitePresidencial(10, 3))

    # Ocupar algunas — ahora con await
    await hotel.habitaciones[1].reservar()  # Master 102
    await hotel.habitaciones[3].reservar()  # SuitePresidencial 104

    print("\n--- Habitaciones disponibles ---")
    for h in hotel.filtrar_habitacion(disponible=True):
        print(h)

    print("\n--- Habitaciones ocupadas ---")
    for h in hotel.filtrar_habitacion(disponible=False):
        print(h)

    print("\n--- Disponibles (comprehension) ---")
    for h in hotel.habitaciones_disponibles():
        print(h)

    print("\n--- Precios ---")
    print(hotel.precio_por_habitacion())

    print("\n--- Resumen ---")
    print(hotel.resumen_ocupacion())

    # ✅ Usa las habitaciones del hotel directamente
    pisos = [
    [h for h in hotel.habitaciones if h.piso == 1],
    [h for h in hotel.habitaciones if h.piso == 2],
    [h for h in hotel.habitaciones if h.piso == 3],
]
    habitaciones = [hab for piso in pisos for hab in piso]
    for hab in habitaciones:
        print(hab)

    # Context manager async
    habitacion = hotel.habitaciones[0]
    async with GestorReservacion(habitacion) as hab:
        print(f"Procesando pago de {hab.numero}...")
        raise ValueError("Pago rechazado")


asyncio.run(main())