import json

produto1 = {
    "nome" : "Sapato",
    "quantidade" : 39,
    "preco" : 10.38,
    "disponibilidade" : True
}

produto2 = {
    "nome" : "Televisao",
    "quantidade" : 10,
    "preco" : 70.38,
    "disponibilidade" : False
}


carrinho: list = []


carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

carrinho_json = json.dumps(carrinho)
print(carrinho_json)