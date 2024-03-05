valor = 1
valor_final = 0
ix = True 

while ix:
    valor = float(input("Digite o valor do produto: "))
    if valor > 0:
        valor_final = valor_final + valor
    elif valor == 0:
      ix = False
    elif valor < 0:
       continue

if valor_final > 1000:
   valor_final = valor_final * 0.10

print(f"O valor total da compra foi de R${valor_final}")

