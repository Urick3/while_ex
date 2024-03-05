soma = 0
cont = 0
ix = True

while ix:
    valor =int(input("Digute um valor ou 0 para finalizar: "))
    if valor != 0: 
        soma = soma + valor
        cont += 1
    else: 
        ix = False

if cont > 0:
    media = soma / cont 
else:
    print("Erro divisão por 0")

print(f"A soma é {soma} e a méda é {media}")    