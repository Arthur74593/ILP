# 18. Leia dois números inteiros. Exiba o maior deles. Se forem iguais, exiba "Os números são iguais".
n1 = int(input("digite um numero:"))
n2 = int(input("digite um numero:"))
maior = max(n1,n2)
if n1==n2:
    print("São iguais")
else:
    print(f"O  maior é {maior}") 