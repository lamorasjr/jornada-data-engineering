import csv
from typing import List


def read_csv(file_name: csv) -> List[dict]:
    '''
    Read a csv file and load the data into a list of dicts.
    '''
    with open(file_name, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        return list(csv_reader)


def process_data(csv_data: List[dict]) -> dict:
    '''
    Process the data and return a dict in which the key is category and the values are a list of dict (product, quantity, and sales amount)
    '''
    categories = {}
    for item in csv_data:
        category = item['Categoria']
        if category not in categories:
            categories[category] = []
        categories[category].append(item)
    return categories


def calc_sales_by_category(dict_data):
    '''
    Calculate the total sales amount by each product categories
    '''
    sales_by_category = {}
    for category, itens in dict_data.items():
        for item in itens:
            sales_amount = sum(int(item['Quantidade']) * int(item['Venda']) for item in itens)
        sales_by_category[category] = sales_amount
    return sales_by_category



# def process_data()
file_path = 'vendas.csv'

csv_data1 = read_csv(file_path)
processed_data = process_data(csv_data1)
total_sales_by_category = calc_sales_by_category(processed_data)

print(total_sales_by_category)
