import pandas as pd

def load_csv_and_filter(csv_file, geo_state):
    # Load a CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Check and remove empty rows 
    df = df.dropna()

    # Fiter rows by the selected geo-state
    df_filtered = df[df['estado'] == geo_state]

    return df_filtered


# Use case example
csv_file = '01-bootcamp-python/module11-15/01-basic/example.csv'  # change this path accordingly with you CSV file
filtered_state = 'SP'
df_filtered = load_csv_and_filter(csv_file, filtered_state)

print(df_filtered)


