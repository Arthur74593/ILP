# 44. Escreva um programa que imprime uma escada de n degraus usando o caractere *. Cada degrau i tem i asteriscos.

degraus = int(input("Quantidade de degraus:"))

for i in range(1,degraus+1):
    print("*"*i)
    

