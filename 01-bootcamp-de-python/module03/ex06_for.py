### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

phrase = "a raposa marrom salta sobre o cachorro preguiçoso"
words = phrase.split()
words_count = {}

for w in words:
    if w in words_count:
        words_count[w] += 1
    else:
        words_count[w] = 1

print(words_count)