from logs import logger
from functools import wraps
from time import time 

def log_situations(level: str = "info"):
    def decorator(func): 
        @wraps(func)
        def wrapper(*args, **kwargs): 
            log = getattr(logger, level)
            log(f"Iniciando: {func.__qualname__}")
            result = func(*args, **kwargs)
            log(f"Completado: {func.__qualname__}")
            return result
        return wrapper
    return decorator

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