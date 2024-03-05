ix = True
maior = 0

while ix:
    num = int(input("Digute um inteiro e positivo ou 0 para finalizar: "))
    if num > maior:
        maior = num

    if num <= 0:
        ix = False 

print(f"O maior número digitado foi {maior}")