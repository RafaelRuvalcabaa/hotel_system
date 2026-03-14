from errors.hotel_errors import NameRest
from logs import logger 
from decoradores import log_action
class Restaurantes: 
    def __init__(self, name_restaurant: str, capacidad_mesa: int)-> None: 
        if name_restaurant == "": 
            logger.error("Restaurantes: Falta Name")
            raise NameRest("No se pudó crear el restaurante por falta de nombre")
        self.name_restaurant = name_restaurant
        self.capacidad_mesa = capacidad_mesa
        self.disponible = True
        logger.info("Restaurantes: CREADO CON EXITO")

    def __str__(self)-> str: 
        return f"Restaruante creado - {self.name_restaurant}"
    
    @log_action
    def reservado(self)-> None: 
        self.disponible = False 
    @log_action
    def liberar(self)-> None: 
        self.disponible = True