# 42. Escreva um programa que recebe um inteiro positivo n e exibe todos os números no intervalo [1, n] que são simultaneamente divisíveis por 2 e por 7.

n = int(input("Digite o numero final do intervalo:"))

for num in range(1,n+1):
    if num % 14 ==0:
        print(num)

    
