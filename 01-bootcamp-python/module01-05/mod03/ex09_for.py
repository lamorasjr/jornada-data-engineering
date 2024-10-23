### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

numbers = range(1,11)

even_numbers = []

# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)

even_numbers = [ number for number in numbers if number % 2 == 0 ]

print(even_numbers)