#06 Encontrar Valores Ausentes em uma Sequência
from typing import List

def find_missing_values(sequence_list: List[int]) -> List[int]:
    list_complement = set(range(min(sequence_list), max(sequence_list) + 1))
    return list(list_complement - set(sequence_list))

sample1 = [1, 4, 5, 10]

sample1_function = find_missing_values(sample1)

print(sample1_function)