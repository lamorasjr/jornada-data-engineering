# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

users = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Carol", "idade": 20},
    {"nome": "Bob", "idade": 25}
]

users.sort(key = lambda users: users['nome'])

print(users)