# 24. Escreva um programa que recebe um número inteiro positivo n e exibe a soma dos dígitos de n.
n = int(input("Digite um numero:"))
soma = 0

for i in str(n):
    soma += int(i)
print(soma)