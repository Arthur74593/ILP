numero = int(input("Quantidade de números na lista"))
lista = list(map(int, input("Digite o números separados por espaço:").split()))
lista_inversa = lista[::-1]

print(*lista_inversa)