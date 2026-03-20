from logs import logger
from errors.hotel_errors import NullFloor, NullNoRoom
from decoradores import  log_situations, timer

class Habitacion: 
    def __init__(self,  numero: int, piso: int, capacidad: int)-> None: 
        if numero <= 0:
            logger.error("Reservacion Hotel: No. Room Null")
            raise NullNoRoom("Numero de habitacion no asignado")
        if piso <= 0: 
            logger.error("No. Piso de Habitacion no asignado")
            raise NullFloor("Reservacion Hotel: No. Floor Null")
        self.numero = numero 
        self.piso = piso 
        self.capacidad = capacidad
        self.disponible = True
        logger.info("Habitacion reservada con exito")

        
    def __str__(self):
        return f"Habitacion {self.numero} - Piso {self.piso} - {'Disponible' if self.disponible else 'Ocupada'}"
    
    @log_situations(level="info")
    def reservar(self):
        self.disponible = False
    @log_situations(level="info")
    def liberar(self): 
        self.disponible = True

    
class Suite(Habitacion): 
    def __init__(self,numero:int, piso:int, precio: float = 1899, capacidad = 2) -> None:
        super().__init__(numero, piso, capacidad) 
        self.precio = precio
        self.servicios = ["WIFI", "TV"]

class Master(Habitacion): 
    def __init__(self,numero: int, piso: int, precio: float = 2599, capacidad = 4) -> None: 
        super().__init__(numero, piso, capacidad)
        self.precio = precio
        self.servicios = ["WIFI", "TV", "Jacuzzi"]


class SuitePresidencial(Habitacion): 
    def __init__(self, numero:int, piso: int, precio: float = 5890, capacidad = 6) -> None: 
        super().__init__( numero, piso, capacidad)
        self.precio = precio
        self.servicios = ["WIFI", "TV", "Sala", "Cocina"]



        