from datetime import date, time
from logs import * 
from errors.hotel_errors import * 


class Person: 
    def __init__(self, first_name: str, middle_name: str | None, last_name: str, address: str, city: str, birth_date: date) -> None:
        if first_name == "": 
            logger.error("Person: No se registro un nombre")
            raise NombreVacioError("No se registró nombre")
        if last_name == "": 
            logger.error("Persona: No se registró apellido")
            raise NombreVacioError("No se registró ninguna apellido")
        
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city 
        self.birth_date = birth_date
    def __str__(self) -> str: 
        return f"{self.first_name} {self.last_name}"
    
class Huesped(Person): 
    def __init__(self, first_name: str, middle_name: str | None, last_name: str, address: str, city: str, birth_date:  date, check_in: date, check_out: date ) -> None: 
        super().__init__(first_name, middle_name, last_name, address, city, birth_date)
        if check_out < check_in: 
            logger.error("Huesped: CheckOut < CheckIn")
            raise CheckInOutError("Valores Erroneos")
        self.check_in = check_in
        self.check_out = check_out
        logger.info("Huesped: CREADO CON EXITO!")

    def __str__(self): 
        return f"{self.first_name} {self.last_name} - Huesped"
     

class Trabajador(Person): 
    def __init__(self, first_name: str, middle_name: str | None, last_name:str, address: str, city: str, birth_date: date , puesto: str, schedule_in: time, schedule_out: time) -> None: 
        super().__init__(first_name, middle_name, last_name, address, city,
                         birth_date)
        if schedule_out < schedule_in: 
            logger.error("Trabajador: Salida < Entrada")
            raise ScheduleError("Schedule Error")
        self.puesto = puesto 
        self.schedule_in = schedule_in
        self.schedule_out = schedule_out
        logger.info("Trabajador: CREADO CON EXITO!")
    def __str__(self): 
        return f"{self.first_name} {self.last_name} - {self.puesto}"
