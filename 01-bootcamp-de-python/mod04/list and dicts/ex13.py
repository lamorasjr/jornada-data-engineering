# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

stock = {
    "Teclado": 10, 
    "Mouse": 0, 
    "Monitor": 3, 
    "CPU": 0
}

positive_stock = {}

for product, quantity in stock.items():
    if quantity > 0:
        positive_stock[product] = quantity

print(positive_stock)
