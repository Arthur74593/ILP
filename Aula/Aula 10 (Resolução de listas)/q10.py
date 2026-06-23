# 10. Escreva um programa que lê 10 números reais digitados pelo usuário e imprime a média aritmética.
soma = 0

for i  in range(10):
      num = int(input("Digite um numero:"))
      soma += num
      media  = soma/10
print(media)
