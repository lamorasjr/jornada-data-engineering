from loguru import logger
from sys import stderr
from functools import wraps

logger.remove()

logger.add(
    "01-bootcamp-python/module06-10/mod09/logs_file.log",
    format="{time} {level} {message} {file}",
    level="INFO"
)

logger.add(
    "01-bootcamp-python/module06-10/mod09/logs_file_critical.log",
    format="{time} {level} {message} {file}",
    level="ERROR"
)

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando função '{func.__name__}' com args {args} e kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função '{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            raise  # Re-lança a exceção para não alterar o comportamento da função decorada
    return wrapper