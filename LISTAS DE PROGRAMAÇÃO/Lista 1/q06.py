numero = int(input("Quantidade de números na lista:"))
lista = list(map(int, input("Digite o números separados por espaço:").split()))

lista.append(lista.pop(0))

print(*lista)