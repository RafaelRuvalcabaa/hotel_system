from logs import logger
from functools import wraps
from time import time 
from errors.hotel_errors import WrapperLogs


def timer(func): 
    @wraps(func)
    def wrapper(*args, **kwargs): 
        start = time()
        result = func(*args, **kwargs)
        final = time() 
        avg = final - start
        logger.info(f"{func.__qualname__} tardó {avg:.4f}s")
        return result
    return wrapper

def validate_input(func): 
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args[1:]:
            if arg is None: 
                logger.error(f"{func.__qualname__}: argumento None detectado")
                raise ValueError(f"{func.__qualname__} recibió un argumento None")
        return func(*args, **kwargs)
    return wrapper





