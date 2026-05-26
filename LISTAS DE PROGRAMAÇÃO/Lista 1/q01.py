# Você recebeu uma fila com N números inteiros. Seu programa deve somar todos os valores da lista 
# e mostrar o resultado final. Para resolver, percorra a lista inteira e acumule a soma em uma variável.

n = int(input("Quantos valores lista ter vai:"))
lista = []

for item in range(n):
    valor = int(input("valor:"))
    lista.append(valor)
soma = 0
for valores in lista:
    soma += valores
print(soma) 