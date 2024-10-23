#5. Preço total da lista de compras

purchase_list = ["maçã", "banana", "cereja"]

prices = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

total = 0
for i in purchase_list:
    total += prices[i]

print(f"Total price: {total}")