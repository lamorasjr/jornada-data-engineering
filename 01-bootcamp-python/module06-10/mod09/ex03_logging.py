from loguru import logger
from sys import stderr

# To display logs in the console
logger.add(
    sink=stderr,
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO"
)

# To save logs in a file
logger.add(
    "01-bootcamp-python/module06-10/mod09/app_logs.log",  # Arquivo onde os logs serão salvos
    format="{time} {level} {message} {file}",
    level="CRITICAL"
)


def soma(x, y):
    try:
        soma = x + y
        logger.info(f'correct values added')
        return soma
    except:
        logger.critical("wrong values, please digit the correct data type")

soma(2,3)
soma(2,"13")