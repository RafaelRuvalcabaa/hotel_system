from datetime import date, time
from models.persona import Trabajador, Huesped
from models.habitacion import Habitacion, Suite, Master, SuitePresidencial
from models.restaurante import Restaurantes
from models.reservacion_restaurante import * 



huesped1 = Huesped(
    "Rafael",
    None,
    "Lopez",
    "Calle 123",
    "CDMX",
    date(2000, 1, 1),
    date(2026, 3, 9),
    date(2026, 3, 12),
)

trabajador1 = Trabajador(
    "Ana",
    "Maria",
    "Perez",
    "Av. Reforma 456",
    "CDMX",
    date(1995, 6, 15),
    "Recepcionista",
    time(4, 0),
    time(8, 0),
)

cliente = Habitacion(101, 1, 2)




print(huesped1)
print(trabajador1)
print(cliente)
