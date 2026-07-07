numero = int(input("Quantidade de números na lista:"))
lista = list(map(int, input("Digite o números separados por espaço:").split()))
x = int(input("Digite um número que pode , ou não, estar na lista:"))

for i in range(len(lista) -1 ,-1 ,-1):
    if lista[i] == x:
        print(i)
        break
else:
    print(-1)


    
