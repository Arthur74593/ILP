n = int(input("quantidade de valores a serem lidos:"))
lista = []

for i in range(n):
    num = int(input("Digite o valor:"))
    lista.append(num)

nova_lista = []
for num in lista:
    if num not in nova_lista:
        nova_lista.append(num)

print(nova_lista)  


