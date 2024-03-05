number = int(input("Digite um número: "))

cont = 0

while number != 0:
    number //= 10
    cont += 1

print("O número total de dígitos é: ", cont)


