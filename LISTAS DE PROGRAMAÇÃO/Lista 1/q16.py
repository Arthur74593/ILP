n = int(input("quantidade de valores a serem lidos:"))
lista = []
m = int(input("quantidade de valores a serem lidos:"))
lista_2 = []

for i in range(n):
    num = int(input("Digite o valor:"))
    lista.append(num)
for i in range(m):
    num = int(input("Digite o valor:"))
    lista_2.append(num)


nova_lista = []
if num in lista and num in lista_2:
    nova_lista += num

print(nova_lista)