import csv

# Path to the csv file
file_path = '01-bootcamp-python/module01-05/mod04/data/exemplo.csv'

# Starts an empty list to store the data
file_data = []

# Use the context manager 'with' to open the file
with open(file_path, mode='r', encoding='utf-8') as file:
    # Create an object to the csv reader
    csv_reader = csv.DictReader(file)

    # Iterate on top on the rows from the csv file
    for row in csv_reader:
        # Add each row (dict type) to a list of data
        file_data.append(row)

# Display the output results from the csv file
for i in file_data:
    print(i)