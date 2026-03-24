import os 

os.system("cls")

soma_notas = 0 
contador = 0

while True:
    
    try:
        nota = float(input("Digite uma nota: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        continue
    
   
    soma_notas += nota
    
   
    contador += 1
    
  
    resposta = input("Deseja inserir mais uma nota? (S/N): ").strip().upper()
    
  
    if resposta == "N":
        break

print("\n--- Resultados ---")

if contador > 0:
    media = soma_notas / contador
    print(f"Quantidade de notas inseridas: {contador}")
    print(f"A média aritmética das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi informada.")
    