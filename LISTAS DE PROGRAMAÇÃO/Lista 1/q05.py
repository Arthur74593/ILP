n = int(input("quantidade de valores a serem lidos:"))
lista = []

for i in range(n):
    num = int(input("Digite o valor:"))
    lista.append(num)
    lista_invertida = lista[::-1]

print(lista_invertida)
