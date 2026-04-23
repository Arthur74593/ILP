# 7. Escreva um programa que recebe um número inteiro positivo n e imprime a soma dos números de 1 a n.
numero = int(input("Digite um numero:"))
x=1
soma=0
if numero>0:
    while x<=numero:
        soma+= x
        x += 1

print("A soma é:",soma)
        