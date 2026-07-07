numero = int(input("Quantidade de números na lista:"))
lista = list(map(int, input("Digite o números separados por espaço:").split()))


lista.insert(0,lista.pop(-1))

print(*lista)