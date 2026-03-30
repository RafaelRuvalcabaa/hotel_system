from datetime import time, date
from models.persona import * 
from models.habitacion import * 
from logs import logger
from errors.hotel_errors import * 
from models.restaurante import Restaurantes

class ReservaRestaurante: 
    def __init__(self, huesped: Huesped, habitacion: Habitacion, restaurante: Restaurantes, num_personas: int, fecha: date, hora: time)-> None: 
        if huesped is None: 
            logger.error("Reserva: No huesped")
            raise NoNameReserva("Error en el huesped - Reserva Restaurante")
        if habitacion is None: 
            logger.error("Reserva: No habitacion")
            raise HabitacionReserva("Error en la habitacion - Reserva Restaurante")
        if num_personas > restaurante.capacidad_mesa: 
            logger.error("Reserva: Mas personas en la mesa de las permitidas.")
            raise MesaError("Mas personas de lo posible")
        self.huesped = huesped
        self.habitacion = habitacion 
        self.num_personas = num_personas 
        self.fecha = fecha
        self.hora = hora 
        logger.info("Reserva: CREADA CON EXITO")

    def __str__(self): 
        return f"Reservacion a nombre de {self.huesped}"
