n = int(input("quantidade de valores a serem lidos:"))
lista = []

for i in range(n):
    num = int(input("Digite o valor:"))
    lista.append(num)
for i in range(len(lista)):
    lista[i] = -lista[i] 

print(lista)
