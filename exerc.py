import os 

os.system("cls")

soma_notas = 0
contador = 0
resposta = "S"

while resposta != "N":
   
    nota = float(input("Digite a nota: "))
    
  
    soma_notas = soma_notas + nota
    

    contador = contador + 1
    

    resposta = input("Deseja inserir mais uma nota? (S/N): ")



media = soma_notas / contador


print("A média aritmética das notas é:", media)