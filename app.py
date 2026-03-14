from datetime import date, time
from models.persona import Trabajador, Huesped
from models.habitacion import Habitacion, Suite, Master, SuitePresidencial
from models.restaurante import Restaurantes
from models.reservacion_hotel import ReservacionHotel
from models.reservacion_restaurante import ReservaRestaurante

# Personas
huesped1 = Huesped("Rafael", None, "Lopez", "Calle 123", "CDMX", date(2000, 1, 1), date(2026, 3, 9), date(2026, 3, 12))
trabajador1 = Trabajador("Ana", "Maria", "Perez", "Av. Reforma 456", "CDMX", date(1995, 6, 15), "Recepcionista", time(8, 0), time(16, 0))

# Habitacion
hab1 = Habitacion(101, 1, 2)

# Reservacion hotel
reserva1 = ReservacionHotel(huesped1, hab1, 2)

# Restaurante
rest1 = Restaurantes("El Mexicano", 4)
rest1.reservado()
rest1.liberar()

# Reservacion restaurante
reserva_rest = ReservaRestaurante(huesped1, hab1, rest1, 2, date(2026, 3, 10), time(14, 0))

print(huesped1)
print(trabajador1)
print(hab1)
print(reserva1)
print(rest1)
print(reserva_rest)