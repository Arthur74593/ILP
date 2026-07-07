def ja_existe(valor, lista):
    return valor in lista

numero = int(input("Quantidade de números na lista:"))
lista = list(map(int, input("Digite o números separados por espaço:").split()))

nova = []

for num in lista:
    if not ja_existe(num, nova):
        nova.append(num)

print(*nova)