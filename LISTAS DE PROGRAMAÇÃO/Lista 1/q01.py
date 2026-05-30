# Você recebeu uma fila com N números inteiros. Seu programa deve somar todos os valores da lista 
# e mostrar o resultado final. Para resolver, percorra a lista inteira e acumule a soma em uma variável.

n = int(input("Quantos valores lista ter vai:"))
itens = input().split()
lista = [int(item) for item in itens]
soma = 0
for numero in lista:
    soma += numero

print(soma)  