# 49. Escreva um programa que lê n valores inteiros e exibe, ao final:

# a soma total,
# a média,
# o maior valor,
# o menor valor,
# a quantidade de valores acima da média.

n = int(input("Digite a quantidade de valores que você quer ler:"))
valores = []


for i in range(n):
    num = int(input())
    valores.append(num)
    soma = sum(valores)
    media = soma/n
    maior = max(valores)
    menor = min(valores)
    contador = 0
for v in valores:
    if v> media:
        contador += 1
print(f'A soma é: {soma}')
print(f'a media é: { media}')
print(f'o maior numero é:{maior}')
print(f'O menor númeir é: {menor}')
print(f'A quantidade de numeros acima da média é: {contador}')
        