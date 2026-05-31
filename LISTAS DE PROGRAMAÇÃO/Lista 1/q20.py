numero = int(input("Quantidade de números na lista:"))
lista = list(map(int, input("Digite o números separados por espaço:").split()))
lista_inversa = lista[::-1]

if lista == lista_inversa:
    print("SIM")
else:
    print("NÃO")