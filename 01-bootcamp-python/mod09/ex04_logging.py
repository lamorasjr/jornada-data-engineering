from utils_log import log_decorator

# @ used also in pydantic and pandera

@log_decorator
def soma(x, y):
    return x + y


soma(2, 3)
soma(2, 7)