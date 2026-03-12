from errors.hotel_errors import NameRest
from logs import logger 
class Restaurantes: 
    def __init__(self, name_restaurant: str, capacidad: int)-> None: 
        if name_restaurant == "": 
            logger.error("Restaurantes: Falta Name")
            raise NameRest("No se pudó crear el restaurante por falta de nombre")
        self.name_restaurant = name_restaurant
        self.capacidad = capacidad
        logger.info("Restaurantes: CREADO CON EXITO")

    def __str__(self)-> str: 
        return f"Restaruante creado - {self.name_restaurant}"
