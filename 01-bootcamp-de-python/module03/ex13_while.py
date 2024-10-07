### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, 
# onde cada "página" de dados é processada em loop até que não haja mais páginas.

current_page = 1
total_pages = 5  # Simulação, na prática, isso viria da API

while current_page <= total_pages:
    print(f'Number of pages processed: {current_page} of {total_pages}')

    current_page += 1

print('All pages have been processed.')