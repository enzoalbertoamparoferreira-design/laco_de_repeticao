import os
os.system("cls")
import time

# Solicita ao usuário um número
numero_str = input("Digite um número para a contagem regressiva: ")

# Verifica se a entrada é um número válido e converte para inteiro
try:
    numero = int(numero_str)
    
    # Faz a contagem regressiva a partir do número informado até 1
    for i in range(numero, 0, -1):
        print(i)
        time.sleep(1)  # Aguarda 1 segundo antes de continuar
        
    print("Contagem finalizada!")

except ValueError:
    print("Por favor, digite um número inteiro válido.")