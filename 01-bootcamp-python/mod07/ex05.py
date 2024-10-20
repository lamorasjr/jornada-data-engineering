#05 - Calcular Desvio Padrão de uma Lista
from typing import List

def std_deviation(values_list: List[float]) -> float:
    avg_value = sum(values_list) / len(values_list)
    deviation_list = [ (x - avg_value) ** 2 for x in values_list ]
    variance = sum(deviation_list) / len(deviation_list)
    return round(variance ** 0.5, 2)


sample1 = [1, 15, 16, 30, 37]

std_deviation_sample1 = std_deviation(sample1)

print(std_deviation_sample1)




