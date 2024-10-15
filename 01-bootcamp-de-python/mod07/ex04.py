#04 - Converter Celsius para Fahrenheit em uma Lista
from typing import List

def convert_celsius_to_fahrenheit(temp_celsius: List[float]) -> float:
    converted_values = []

    for temp in temp_celsius:
        convertion = round( (9/5) * temp + 32, 1 )
        converted_values.append(convertion)
    
    return converted_values


ex_list = [1, 15, 16, 30, 37]

ex_result = convert_celsius_to_fahrenheit(ex_list)
print(ex_result)