# 41. Leia três números inteiros e exiba-os em ordem crescente usando apenas estruturas de seleção.

n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número"))
n3 = int(input("Digite outro número"))

if n3<n2<n1:
    print(n3,n2,n1)
elif n1<n2<n3:
    print(n1,n2,n3)
elif n2<n1<n3:
    print(n2,n1,n3)
elif n3<n1<n2:
    print(n3,n1,n2)
elif n3==1:
    print("cleiton")