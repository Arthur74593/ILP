# 45. Escreva um programa que recebe dois inteiros inicio e fim e exibe a soma de todos os números primos no intervalo [inicio, fim].

inicio = int(input("DIgite o inicio:"))
final = int(input("DIgite o final:"))
soma = 0


for i in range(inicio,final+1):
    if i<2:
        continue
    for n in range(2,i):
        if i%n==0:
            break
    else:
        soma += i
          
print(soma)
    