# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dicts = {**dict1, **dict2}

print(merged_dicts)