n, k = map(int, input().split())
lista = list(map(int, input().split()))
dicio = {}
nova_lista = []

for i, valor in enumerate(lista):
    if valor in dicio:
        dicio[valor] += 1
    else:
        dicio[valor] = 1

    if dicio[valor] <= k: 
        nova_lista.append(valor)

print(*nova_lista)