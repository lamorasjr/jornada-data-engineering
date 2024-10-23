### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

maximum_attemps = 5
attempt_number = 1

while attempt_number <= maximum_attemps:
    print(f'Connection attempt(s): {attempt_number} of {maximum_attemps}')

    if False:
        print('Connection sucessfully established.')
        break
    
    attempt_number += 1
else:
    print('Failed to connect after multiple attempts.')