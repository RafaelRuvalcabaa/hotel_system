from models.persona import Huesped
from models.habitacion import Habitacion
from errors.hotel_errors import UnknowHuesped, UnknowRoom, OverFlow
from logs import logger 
from decoradores import validate_input
import asyncio


class ReservacionHotel: 
    @validate_input
    def __init__(self, huesped: Huesped, habitacion: Habitacion, num_personas: int)-> None: 
        if num_personas > habitacion.capacidad:
            logger.error("Reservacion Hotel: Capacidad excedida")
            raise OverFlow("El numero de personas son mayor al permitido")
        self.huesped = huesped
        self.habitacion = habitacion
        self.num_personas = num_personas
        self.habitacion.reservar()
        logger.info("Reservacion Hotel: CREADA CON EXITO")

    def __str__(self): 
        return f"Habitacion reservada a nombre de {self.huesped}"

