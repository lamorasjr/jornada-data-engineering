#02 - Filtrar Dados Acima de um Limite

from typing import List


def filter_greater_than(values_list: List[float], lower_limit: float) -> List[float]:
    result_list = []

    for v in values_list:
        if v > lower_limit:
            result_list.append(v)
    
    return result_list


ex_list = [1, 15, 16, 30, 50]

ex_result = filter_greater_than(ex_list, 18)
print(ex_result)

