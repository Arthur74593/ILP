n = int(input("quantidade de valores a serem lidos:"))
lista = []

for i in range(n):
    num = int(input("Digite o valor:"))
    lista.append(num)
if len(lista) > 1:
    ultimo  = lista.pop(-1)
    lista.insert(0, ultimo)

print(lista)