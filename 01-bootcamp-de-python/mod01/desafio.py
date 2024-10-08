"""
DESAFIO: Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.
"""

CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite o seu nome
nome_usuario = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario_usuario = float(input("Digite o seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite o seu bonus: "))

# 4) Calcule o valor do bônus final
valor_do_bonus = CONSTANTE_BONUS + ( salario_usuario * bonus_usuario )

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bônus
print(f"O usuário {nome_usuario} recebeu o bônus de {valor_do_bonus}")