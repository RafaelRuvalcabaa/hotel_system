
from models.habitacion import Habitacion, Suite, Master, SuitePresidencial

class Hotel: 
    def __init__(self, name_hotel: str)-> None: 
        self.name_hotel = name_hotel
        self.habitaciones = []
    
    def agregar_habitacion(self, habitacion: Suite| Master | SuitePresidencial ):
        self.habitaciones.append(habitacion)

    def filtrar_habitacion(self, disponible: bool = True):
            for h in self.habitaciones:
                if h.disponible == disponible:
                    yield h 
    

        
