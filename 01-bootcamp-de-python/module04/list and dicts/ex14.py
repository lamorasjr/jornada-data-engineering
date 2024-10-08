# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

dict_sample = {
    "a": 1, 
    "b": 2, 
    "c": 3
}

dict_keys = list( dict_sample.keys() )

dict_values = list( dict_sample.values() )

print("Chaves:", dict_keys)
print("Valores:", dict_values)