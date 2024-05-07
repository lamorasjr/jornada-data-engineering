produto1: str = "sapato"
produto2: str = "camiseta"
produto3: str = "videogame"

produtos: list = []

# adicionando produtos a lista

produtos.append(produto1)
produtos.append(produto2)
produtos.append(produto3)

print(produtos)

# removendo o ultimo item da lista

produtos.pop()
produtos.pop()

print(produtos)



numeros = []
# adicionando um range de items na lista
numeros.extend(range(0,5))

print(numeros)