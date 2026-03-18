import os 

os.system("cls")

notas = []


for i in range(1, 4):
    while True:
        try:
            nota = float(input(f"Digite a nota {i} (0 a 10): "))
            
         
            if 0 <= nota <= 10:
                notas.append(nota)
                break  
            else:
                print("Valor inválido. A nota deve ser entre 0 e 10. Tente novamente.\n")
        
        except ValueError:
            
            print("Entrada inválida. Por favor, digite um número.\n")


media = sum(notas) / len(notas)


print(f"\nMédia final: {media:.2f}")


if media >= 7:
    print("Situação: Aprovado")
elif media >= 5: 
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")