# Leia um número inteiro positivo N. Calcule e imprima a soma de todos os inteiros de 1 até N.

# Exemplo:
# Entrada: 10
# Saída: 55

n = int(input("Digite n: "))
i = 1 
soma = 0

while i <= n:
    soma += i
    i += 1
print(soma)