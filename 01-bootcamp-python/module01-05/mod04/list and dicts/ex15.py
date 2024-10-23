# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

sample_text = "engenharia de dados"
freq = {}

for character in sample_text:
    if character in freq:
        freq[character] += 1
    else:
        freq[character] = 1

print(freq)