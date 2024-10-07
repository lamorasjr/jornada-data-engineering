### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

vendas_groupby = {}

for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    
    if categoria in vendas_groupby:
        vendas_groupby[categoria] += valor
    else:
        vendas_groupby[categoria] = valor


print(vendas_groupby)