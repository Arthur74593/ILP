# 40. Escreva um programa que recebe um inteiro positivo n 
# e determina se n é um número perfeito (um número é perfeito se
#  a soma de seus divisores próprios é igual a ele mesmo, ex: 6 = 1+2+3).

n = int(input("Digite um número: "))

soma = 0

for i in range(1, n):
    if n % i == 0:
        soma += i

if soma == n:
    print("É um número perfeito")
else:
    print("Não é um número perfeito")