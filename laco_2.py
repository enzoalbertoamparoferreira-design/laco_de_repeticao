import os 

os.system("cls")

login_correto = "admin"
senha_correta = "12345"

while True:
  
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    
    
    if login == login_correto and senha == senha_correta:
        print("Acesso concedido! Bem-vindo(a).")
        break 
    else:
        
        print("Login ou senha incorretos. Por favor, tente novamente.\n")