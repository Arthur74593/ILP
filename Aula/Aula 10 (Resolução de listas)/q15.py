# 15. Escreva um programa que lê números inteiros do usuário enquanto o usuário não digitar 0, e ao final exibe a quantidade de números lidos (sem contar o zero).
num = int(input("Digite um número:"))
contador = 0

while num != 0:
    contador += 1
    num = int(input("Digite um número: "))

print("Quantidade de números digitados:", contador)
    