#10. Divisão de Dados em Grupos
#Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = [ n for n in numbers if n % 2 == 0 ]
odd = [ n for n in numbers if n % 2 != 0 ]

print("Pares:", even)
print("Ímpares:", odd)