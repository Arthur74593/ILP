numero = int(input("Quantidade de números na lista:"))
lista = list(map(int, input("Digite o números separados por espaço:").split()))

menor = lista[0]
maior = lista[0]

for num in lista:
    if num < menor:
        menor = num
    if num > maior:
        maior = num

print(menor, maior)



