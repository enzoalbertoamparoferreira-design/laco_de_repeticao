import os 

os.system("cls")

while True:
  
    nota = float(input("Digite a nota do aluno (0 a 10): "))
 
    if nota >= 0 and nota <= 10:
        break 
    else:
       
        print("Nota inválida! Por favor, insira um valor entre 0 e 10.\n")

print(f"A nota informada pelo usuário foi: {nota}")