n = int(input("Quantos valores lista ter vai:"))
itens = input().split()
lista = [int(item) for item in itens]
soma = 0
for numero in lista:
    soma += numero

print(soma)                                                                                                                                                                        n = int(input("Quantos valores lista ter vai:"))



lista = []

for item in range(n):
    valor = int(input("valor:"))
    lista.append(valor)
soma = 0
for valores in lista:
    soma += valores
print(soma)  
