num = int(input("Quantos números da sequência de Fibonacci você deseja exibir? "))

if num <= 0:
    print("Por favor, insira um número maior que 0.")
elif num == 1:
    print("Sequência de Fibonacci com 1 termo:", end=" ")
    print(0)
else:
    primeiro = 0
    segundo = 1
    
    print("Sequência de Fibonacci com", num, "termos:", end=" ")
    print(primeiro, segundo, end=" ")
    cont = 2
    while cont < num:
        proximo = primeiro + segundo
        primeiro = segundo 
        segundo = proximo
        print(proximo, end=" ") 
        cont += 1
