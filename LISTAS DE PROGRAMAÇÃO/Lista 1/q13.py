numero = int(input("Quantidade de números na lista:"))
lista = list(map(int, input("Digite o números separados por espaço:").split()))

for i in range(len(lista)):
    if lista[i] < 0:
        lista[i] = 0 
print(*lista)
    
