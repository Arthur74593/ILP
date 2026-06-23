# 13. Escreva um programa que recebe um número inteiro positivo n e imprime os múltiplos de 3 entre 1 e n.
num = int(input("Digite um número: "))

for i in range(1,num+1):
    if i%3==0:
        print(i)