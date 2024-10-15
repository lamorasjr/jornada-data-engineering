#03 - Contar Valores Únicos em uma Lista
from typing import List

def count_unique_values(values_list: List[int]) -> int:
    return len(set(values_list))

ex_list = [1, 15, 16, 30, 50, 50, 16]

ex_result = count_unique_values(ex_list)
print(ex_result)