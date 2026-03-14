from logs import logger
from functools import wraps

def log_action(func): 
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Iniciando: {func.__qualname__}")
        result = func(*args, **kwargs)
        logger.info(f"Completado: {func.__qualname__}")
        return result
    return wrapper

