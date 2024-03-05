ix = True
soma = 0

while ix:
    num = int(input("Digute um valor ou 0 para finalizar: "))
    soma = soma + num 
    if num == 0:
        ix = False

print(f"A soma de todos os valores é {soma}")