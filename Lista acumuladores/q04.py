# Leia um número inteiro não-negativo N. Calcule e imprima o valor de N! (fatorial de N). Considere que 0! = 1.

# Exemplo:

# Entrada: 5
# Saída: 120

n = int(input("Digite o número:"))
fat = 1


if n > 0:
    for i in range(1, n + 1):
        fat *= i
    print(fat)
elif n == 0:
    print(1)
else:
    print("Não se pode ter fatorial negativo")
