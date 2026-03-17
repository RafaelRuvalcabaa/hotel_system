from datetime import date, time
from models.persona import Trabajador, Huesped
from models.habitacion import Habitacion, Suite, Master, SuitePresidencial
from models.restaurante import Restaurantes
from models.reservacion_hotel import ReservacionHotel
from models.reservacion_restaurante import ReservaRestaurante
from models.hotel import Hotel



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

# Ocupar algunas
hotel.habitaciones[1].reservar()  # Master 102 ocupada
hotel.habitaciones[3].reservar()  # SuitePresidencial 104 ocupada

print("\n--- Habitaciones disponibles ---")
for h in hotel.filtrar_habitacion(disponible=True):
    print(h)

print("\n--- Habitaciones ocupadas ---")
for h in hotel.filtrar_habitacion(disponible=False):
    print(h)