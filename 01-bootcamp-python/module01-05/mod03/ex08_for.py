### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, 
# filtrar aqueles que têm um campo específico faltando

users = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

valid_users = []

for user in users:
    if user['email']:
        valid_users.append(user)

print(valid_users)