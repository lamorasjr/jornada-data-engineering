from loguru import logger

# Different levels of log messages
logger.debug("Isso é uma mensagem de debug / This is a bug message")
logger.info("Isso é uma mensagem informativa / This is an informative message")
logger.warning("Isso é um aviso / This is a warning message")
logger.error("Isso é um erro / This is an error message")
logger.critical("Isso é crítico / This is an critical message")

# the output will display in the console