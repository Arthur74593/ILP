numero = int(input("Quantidade de números na lista"))
lista = list(map(int, input("Digite o números separados por espaço:").split()))
pares = 0
for num in lista:
    if num % 2 == 0:
        pares += 1

print(pares)

    