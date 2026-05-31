numero = int(input("Quantidade de números na lista:"))
lista = list(map(int, input("Digite o números separados por espaço:").split()))
x = int(input("Digite um número que pode , ou não, estar na lista:"))

if x in lista:
    posicao = lista.index(x)
    print(posicao)
else:
    print(-1)