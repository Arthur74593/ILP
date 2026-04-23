# 6. Escreva um programa que recebe um número inteiro positivo n como entrada e imprime todos os inteiros de 1 a n.
numero = int(input("Digite um numero:"))
x=1

if numero>0:
    while x<=numero:
        print(x)
        x = x+1
else:
    print("O numero tem que ser positivo")