from logs import logger 
from functools import wraps
from errors.hotel_errors import WrapperLogs

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        name_func = func.__name__
        logger.info(f"Executing function: {name_func}")
        try:
            result = func(*args, **kwargs)
            logger.info("The function executed succeful")
            return result
        except Exception as error: 
            logger.error(f"The function - {name_func}- had a problem")
            raise WrapperLogs(f"Error en {name_func}") from error
    return wrapper

        

            