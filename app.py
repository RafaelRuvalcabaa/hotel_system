from datetime import date, time
from models.persona import Trabajador, Huesped
from models.habitacion import Habitacion, Suite, Master, SuitePresidencial
from models.restaurante import Restaurantes
from models.reservacion_hotel import ReservacionHotel
from models.reservacion_restaurante import ReservaRestaurante
from models.hotel import Hotel
from errors.hotel_errors import BadOperation
from contexts_manager import GestorReservacion



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

print("\n--- Disponibles (comprehension) ---")
for h in hotel.habitaciones_disponibles():
    print(h)

print("\n--- Precios ---")
print(hotel.precio_por_habitacion())

print("\n--- Resumen ---")
print(hotel.resumen_ocupacion())

pisos = [
    [Suite(101, 1), Suite(103, 1), Suite(105, 1)],   # piso 1
    [Master(102, 2), Master(106, 2)],                  # piso 2
    [SuitePresidencial(104, 3), SuitePresidencial(10, 3)]  # piso 3
]

habitaciones = [hab for piso in pisos for hab in piso]

for hab in habitaciones:
    print(hab)


habitacion = hotel.habitaciones[0]  # Suite 101

with GestorReservacion(habitacion) as hab:
    print(f"Procesando pago de {hab.numero}...")
    raise ValueError("Pago rechazado")