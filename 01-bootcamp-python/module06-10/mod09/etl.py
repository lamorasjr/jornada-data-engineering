import pandas as pd
import os
import glob
from utils_log import log_decorator

# Function that extracts, read and consolidates json file
@log_decorator
def extract_data(folder: str) -> pd.DataFrame:
    json_files = glob.glob(os.path.join(folder, '*.json'))
    df_list = [ pd.read_json(file) for file in json_files ]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

# Function to transform
@log_decorator
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df['Total'] = df['Quantidade'] * df['Venda']
    return df

# Function to load in CSV or Parquet
@log_decorator
def load_data(df: pd.DataFrame, output_formats: list):
    for format in output_formats:
        if format == 'csv':
            df.to_csv('01-bootcamp-python/module06-10/mod09/sample_data.csv')
        if format == 'parquet':
            df.to_parquet('01-bootcamp-python/module06-10/mod09/sample_data.parquet', index=False)

@log_decorator
def pipeline_calculate_sales_kpi_consolidated(folder: str, output_formats: list):
        df_raw = extract_data(folder)
        df_transformed = transform_data(df_raw)
        load_data(df_transformed, output_formats)
        print("ETL successfully completed.")


# if __name__ == '__main__':
#     files_folder1: str = 'data'
#     output_formats1: list = ['csv', 'parquet']
#     pipeline_calculate_sales_kpi_consolidated(files_folder1, output_formats1)