import pandas as pd

class ProcessCSV:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.df = None

    def load_csv(self):
        # Load the CSV file into a DataFrame
        self.df = pd.read_csv(self.csv_file)

    def remove_empty_rows(self):
        # Check and remove empty rows
        self.df = self.df.dropna()

    def filter_by_geo_state(self, geo_state):
        # Fiter rows by the selected geo-state
        self.df = self.df[self.df['estado'] == geo_state]

    def process_csv(self, geo_state):
        # Load CSV, remove empty rows and filter by geo-state
        self.load_csv()
        self.remove_empty_rows()
        self.filter_by_geo_state(geo_state)

        return self.df

# Use case example
csv_file = '01-bootcamp-python/module11-15/01-basic/example.csv'
geo_state = 'SP'

file_to_process = ProcessCSV(csv_file)
df_filtered = file_to_process.process_csv(geo_state)

print(df_filtered)