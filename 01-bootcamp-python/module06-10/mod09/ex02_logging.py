from loguru import logger
from sys import stderr

logger.add("01-bootcamp-python/module06-10/mod09/my_app_log")

def soma(x, y):
    try:
        soma = x + y
        logger.info(f'correct values added')
        return soma
    except:
        logger.critical("wrong values, please digit the correct data type")

soma(2,3)
soma(2,7)
soma(2,"3")