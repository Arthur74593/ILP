numero = int(input("Quantidade de números na lista:"))
lista = list(map(int, input("Digite o números separados por espaço:").split()))
maior_diferenca  = abs(lista[1]-lista[0])

for i in range(1,len(lista)):
    direferenca = abs(lista[i]-lista[i-1])

    if direferenca>maior_diferenca:
        maior_diferenca = direferenca
print(maior_diferenca)
