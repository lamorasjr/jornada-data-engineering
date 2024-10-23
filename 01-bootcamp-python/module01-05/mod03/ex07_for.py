### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

numbers = [10, 20, 30, 40, 50]
minimum = min(numbers)
maximum = max(numbers)

normalization = [(x - minimum) / (maximum - minimum) for x in numbers]

print(normalization)