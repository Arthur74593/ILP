n = int(input("Quantidade de valores a serem lidos:"))
lista = []
pares = 0
for i in range(n):
    num = int(input("valor:"))
    lista.append(num)
    if num % 2 == 0:
        pares += 1
print(pares)