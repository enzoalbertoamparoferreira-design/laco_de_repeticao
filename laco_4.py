import os 

os.system("cls")
login_correto = "admin"
senha_correta = "1234"


for tentativa in range(3):
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
  
    if login == login_correto and senha == senha_correta:
        print("Acesso concedido! Bem-vindo.")
        break 
    else:
        tentativas_restantes = 2 - tentativa
        if tentativas_restantes > 0:
            print(f"Login ou senha incorretos. Você ainda tem {tentativas_restantes} tentativa(s).\n")
        else:
            print("Número máximo de tentativas atingido. Acesso bloqueado e programa finalizado.")