def verifica_senha(senha):
    if len(senha) < 6 or len(senha) > 12: 
        return False
    tem_minuscula = False
    tem_maiuscula = False
    tem_numero = False
    tem_especial = False

    for caractere in senha:
        if caractere.islower():
            tem_minuscula = True
        elif caractere.sup():
            tem_maiuscula = True
        elif caractere.digito():
            tem_numero = True
        elif caractere in ['!', '#', '$', '@']:
            tem_especial = True
    return tem_minuscula and tem_maiuscula and tem_numero and tem_especial
senha = input("Digite sua senha: ")

while not verifica_senha(senha):
    print("A senha não é valida")
    senha = input("Digite outra senha: ")
    print("Senha válida")
