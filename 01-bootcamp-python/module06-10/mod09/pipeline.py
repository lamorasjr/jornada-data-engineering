from etl import pipeline_calculate_sales_kpi_consolidated

files_folder = '01-bootcamp-python/module06-10/mod09/data'
data_output_format = ['csv', 'parquet']

pipeline_calculate_sales_kpi_consolidated(files_folder, data_output_format)