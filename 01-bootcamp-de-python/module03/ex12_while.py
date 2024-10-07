### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.


number = int(input("Insert a number between 1 and 10: "))

while number < 1 or number > 10:
    print("Number out of the interval!")

    number = int(input("Please, insert a number between 1 and 10: "))

print("Valid number!")