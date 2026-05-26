# Leia um número inteiro positivo N. Calcule e imprima a soma de todos os inteiros de 1 até N.

# Exemplo:
# Entrada: 10
# Saída: 55

n = int(input("Digite onúmero:"))
soma =0

for i in range(1,n+1):
    soma += i

print(soma)
