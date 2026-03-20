# P ersonas 
class NombreVacioError(Exception): pass
class CheckInOutError(Exception): pass
class ScheduleError(Exception): pass
# Habitacion 
class NullHuesped(Exception): pass 
class NullNoRoom(Exception): pass 
class NullFloor(Exception): pass 
# Reservacion Hotel
class UnknowHuesped(Exception): pass 
class UnknowRoom(Exception): pass 
class OverFlow(Exception): pass 

# Creacion Restaurante 
class NameRest(Exception): pass 

# Reservacion Restaurante 
class NoNameReserva(Exception): pass 
class HabitacionReserva(Exception): pass 
class MesaError(Exception): pass 


# Contex Manager 

class BadOperation(Exception): pass 
