n = int(input())
lista = list(map(int, input().split()))
sequencia = 1
maior_trecho = 1

for i in range(1, n):
    if lista[i] > lista[i - 1]:
        sequencia += 1
        if maior_trecho < sequencia: maior_trecho = sequencia 
    else: 
        sequencia = 1

print(maior_trecho)