# 25. Escreva um programa que recebe um número inteiro positivo n e exibe n na ordem inversa dos dígitos.
n = int(input("Digite um número: "))

invertido = 0

while n > 0:
    digito = n % 10
    invertido = invertido * 10 + digito
    n //= 10

print("Número invertido:", invertido)
    