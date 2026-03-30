from models.habitacion import * 
from decorators import log_execution
import asyncio


class GestorReservacion:
    def __init__(self, habitacion: Habitacion)-> None:
        self.habitacion = habitacion

    async def __aenter__(self):
        await self.habitacion.reservar()
        print(f"Habitacion {self.habitacion.numero} reservada")
        return self.habitacion
    
    async def __aexit__(self, exc_type, exc_val, tb_tb):
        if exc_type is not None: 
            await self.habitacion.liberar()
            print("Something fail - Your reservation couldnt was accepted")
        return False 
    