# Crie uma estrutura para armazenar informacoes de um livro
# inclua titulo, autor e ano de publicacao
# Imprima cada informacao


from typing import Dict, Any

livro: dict[str, Any] = {
    "titulo" : "senhor dos aneis",
    "autor" : "tolkien",
    "ano" : 2005
}


for e in livro.items():
    print(e)