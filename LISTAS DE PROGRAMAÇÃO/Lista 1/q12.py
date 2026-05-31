numero = int(input("Quantidade de números na lista:"))
lista = list(map(int, input("Digite o números separados por espaço:").split()))
lista_nova = []

for num in lista:
    lista_nova.append(-num)

print(*lista_nova)
