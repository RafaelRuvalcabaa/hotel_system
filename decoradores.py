import asyncio
from logs import logger
from functools import wraps
from time import time


def log_situations(level: str = "info"):
    def decorator(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            log = getattr(logger, level)
            log(f"Iniciando: {func.__qualname__}")
            result = await func(*args, **kwargs)
            log(f"Completado: {func.__qualname__}")
            return result

        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            log = getattr(logger, level)
            log(f"Iniciando: {func.__qualname__}")
            result = func(*args, **kwargs)
            log(f"Completado: {func.__qualname__}")
            return result

        # Detecta si la función decorada es coroutine y elige el wrapper correcto
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper

    return decorator


def timer(func):
    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        start = time()
        result = await func(*args, **kwargs)
        final = time()
        logger.info(f"{func.__qualname__} tardó {final - start:.4f}s")
        return result

    @wraps(func)
    def sync_wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        final = time()
        logger.info(f"{func.__qualname__} tardó {final - start:.4f}s")
        return result

    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    return sync_wrapper


def validate_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args[1:]:
            if arg is None:
                logger.error(f"{func.__qualname__}: argumento None detectado")
                raise ValueError(f"{func.__qualname__} recibió un argumento None")
        return func(*args, **kwargs)
    return wrapper