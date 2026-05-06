# 48. Escreva um programa que recebe um inteiro positivo n e verifica se ele é um palíndromo numérico (lê-se igual de trás para frente).

n = int(input("Digite um número:"))
n = list(n)
n_inv = reversed(n)

while 