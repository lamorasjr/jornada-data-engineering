### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

temperature = 22

if temperature < 18:
    print('Baixa')
elif 18 <= temperature <= 26:
    print('Normal')
else:
    print('Alta')