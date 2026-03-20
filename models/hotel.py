
from models.habitacion import Habitacion, Suite, Master, SuitePresidencial

class Hotel: 
    def __init__(self, name_hotel: str)-> None: 
        self.name_hotel = name_hotel
        #Aqui se guardan todas las habitaciones
        self.habitaciones = []
    
    
    def agregar_habitacion(self, habitacion: Suite| Master | SuitePresidencial ):
        #Aqui se enlaza self.habitaciones con mi archivo habitacion por lo tanto accedes a todos los metodos. Suite, Master, SuitePresidencial
        self.habitaciones.append(habitacion)

    def filtrar_habitacion(self, disponible: bool = True):
            for h in self.habitaciones:
                if h.disponible == disponible:
                    yield h 

    def habitaciones_disponibles(self)-> list: 
        looking = [h for h in self.habitaciones if h.disponible]
        return looking 

    def precio_por_habitacion(self)-> dict: 
         price = {h.numero: h.precio for h in self.habitaciones }
         return price 
    def resumen_ocupacion(self)-> dict: 
         disponibles = [h for h in self.habitaciones if h.disponible]
         ocupadas = [h for h in self.habitaciones if not h.disponible]
         return {"disponibles": len(disponibles), "ocupadas": len(ocupadas) }