# 8. Escreva um programa que recebe um número inteiro positivo n e imprime o produto (fatorial) de 1 × 2 × ... × n.
n = int(input("Digite um número: "))

fatorial = 1

for i in range(1, n + 1):
    fatorial *= i

print("Fatorial:", fatorial)