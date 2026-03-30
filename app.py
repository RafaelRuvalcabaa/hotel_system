import asyncio
from models.hotel import Hotel
from factories.habitacion_factory import HabitacionFactory

async def main():
    hotel = Hotel("Camino Real")

    # Todas las habitaciones con Factory
    hotel.agregar_habitacion(HabitacionFactory.build("suite", 101, 1))
    hotel.agregar_habitacion(HabitacionFactory.build("master", 102, 2))
    hotel.agregar_habitacion(HabitacionFactory.build("suite", 103, 1))
    hotel.agregar_habitacion(HabitacionFactory.build("presidencial", 104, 3))
    hotel.agregar_habitacion(HabitacionFactory.build("suite", 105, 1))
    hotel.agregar_habitacion(HabitacionFactory.build("master", 106, 2))
    hotel.agregar_habitacion(HabitacionFactory.build("suite", 107, 1))
    hotel.agregar_habitacion(HabitacionFactory.build("presidencial", 108, 3))

    await hotel.habitaciones[1].reservar()
    await hotel.habitaciones[3].reservar()

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

    pisos = [
        [h for h in hotel.habitaciones if h.piso == 1],
        [h for h in hotel.habitaciones if h.piso == 2],
        [h for h in hotel.habitaciones if h.piso == 3],
    ]
    habitaciones = [hab for piso in pisos for hab in piso]
    for hab in habitaciones:
        print(hab)


asyncio.run(main())