import csv


caminho_do_arquivo: str = "arquivos/exemplo.csv"

arquivo_csv: list = []

with open(file=caminho_do_arquivo, mode="r", encoding="utf-8") as arquivo:
    leitor_de_csv: csv.DictReader = csv.DictReader(arquivo)

    for linha in leitor_de_csv:
        arquivo_csv.append(linha)


print(arquivo_csv)