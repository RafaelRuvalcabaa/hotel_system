from models.habitacion import * 


class GestorReservacion:
    def __init__(self, habitacion: Habitacion)-> None:
        self.habitacion = habitacion

    def __enter__(self):
        self.habitacion.reservar()
        print(f"Habitacion {self.habitacion.numero} reservada")
        return self.habitacion
    
    def __exit__(self, exc_type, exc_val, tb_tb):
        if exc_type is not None: 
            self.habitacion.liberar()
            print("Something fail - Your reservation couldnt was accepted")
        return False 
    