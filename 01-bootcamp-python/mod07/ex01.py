#01 - Calcular Média de Valores em uma Lista
from typing import List

def list_avg(values_list: List[float]) -> float:
    '''
    calculates the average of a list of numbers and returns float
    '''
    avg_value = sum(values_list) / len(values_list)
    return avg_value


list_numbers = [1, 10, 5, 4]

numbers_avg = list_avg(list_numbers)
print(numbers_avg)