# 14. Escreva um programa que recebe um número inteiro base e um número inteiro positivo expoente, 
# e calcula base ** expoente sem usar o operador ** — use apenas multiplicações repetidas com while.

num = int(input("Digite um número: "))
expoente = int(input("Digite outro número:"))
resultado =  1
contador  = 0

while contador < expoente:
    resultado *= num
    contador+=1
print(f"resultado:{resultado}")

