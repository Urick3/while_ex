senha_correta = input("Digite a senha")

senha_confirmacao = input("Digite a senha novamete")

while senha_correta != senha_confirmacao:
    print("As senhas não correspondem. Tente novamente")
    senha_correta = input("Digite a senha: ")
    senha_confirmacao = input("Digite a senha novamente: ") 
else:
    print("As senhas correspondem. Bem-Vindo")