numero = int(input("Quantidade de números na lista:"))
lista = list(map(int, input("Digite o números separados por espaço:").split()))

lista_nova = set(lista)
mais_uma = list(lista_nova)

print(*mais_uma)