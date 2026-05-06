# 48. Escreva um programa que recebe um inteiro positivo n e verifica se ele é um palíndromo numérico (lê-se igual de trás para frente).
n = int(input("Digite um número:"))
lista = list(str(n))
n_inv = list(reversed(lista))

if lista == n_inv:
    print("É palindromo")
else:
    print("Não é palindromo")
