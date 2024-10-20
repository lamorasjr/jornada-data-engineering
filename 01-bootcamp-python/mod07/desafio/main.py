from etl import read_csv, process_data, calc_sales_by_category

# Path of input file
file_path = 'vendas.csv'

csv_data1 = read_csv(file_path)
processed_data = process_data(csv_data1)
total_sales_by_category = calc_sales_by_category(processed_data)
for categoria, total in total_sales_by_category.items():
    print(f'{categoria}: ${float(total)}')