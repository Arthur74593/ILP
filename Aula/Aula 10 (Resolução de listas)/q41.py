# 41. Escreva um programa que lê n pares de números inteiros (a, b) e, para cada par, informa qual é o maior, qual é o menor, ou se são iguais.

n = int(input("Quantos pares você quer analisar? "))

for i in range(n):
    print(f"\nPar {i+1}:")
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    if a > b:
        print(f"Maior: {a} | Menor: {b}")
    elif b > a:
        print(f"Maior: {b} | Menor: {a}")
    else:
        print("Os dois números são iguais")
