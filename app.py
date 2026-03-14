from datetime import date, time
from models.persona import Trabajador, Huesped
from models.habitacion import Habitacion, Suite, Master, SuitePresidencial
from models.restaurante import Restaurantes

from models.reservacion_restaurante import * 



rest = Restaurantes("El Mexicano", 4)
rest.reservado()
rest.liberar()



hab = Habitacion(101, 1, 2)
hab.reservar()
hab.liberar()