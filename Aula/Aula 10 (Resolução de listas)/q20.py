# 20. Escreva um programa que calcula e exibe a soma: 1 + 1/2 + 1/3 + 1/4 + ... + 1/n, onde n é fornecido pelo usuário.

quantidade = int(input("Digite a quantidade de loops:"))
divisor = 1
soma = 0

for i in range(1,quantidade+1):
    soma+= 1/i

print(f"A soma é: {soma}")
