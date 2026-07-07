# 17. Escreva um programa que recebe dois inteiros positivos a e b (com a < b) e imprime todos os inteiros no intervalo [a, b].
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

for indice in range(a, b + 1):
    print(indice)