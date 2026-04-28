# 11. Escreva um programa que recebe um número inteiro positivo n e imprime a tabuada de multiplicação de n (de 1 a 10).
num = int(input("Digite um número: "))

for indice in range(1, 11):
    print(f"{num} x {indice} = {num * indice}")