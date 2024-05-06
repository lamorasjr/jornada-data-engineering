### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = "hoje e o a nossa segunda aula do bootcamp , bootcamp de python"

palavras = texto.split()    # split() sem argumento, divide por " "


contagem_de_palavras = {}

for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] = +1
    else:
        contagem_de_palavras[palavra] = 1