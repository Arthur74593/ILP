# 43. Escreva um programa que lê números inteiros positivos do usuário enquanto o usuário não digitar um valor negativo,
#  e ao final exibe quantos dos números lidos são pares e quantos são ímpares.

num = int(input("Digite um número (negativo para parar): "))

#contadores
pares = 0
impares = 0

while num >= 0:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    num = int(input("Digite um número (negativo para parar): "))

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")



