# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

ages = [22, 15, 30, 17, 18]

valid_ages = []

for age in ages:
    if age >= 18:
        valid_ages.append(age)

print(valid_ages)