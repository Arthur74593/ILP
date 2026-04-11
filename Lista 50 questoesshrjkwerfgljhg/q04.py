# 4. Leia um número inteiro. Se ele for par, exiba "O número é par".

numero = int(input("digite um numero:"))

if numero%2==0:
    print("o  numero é par")
elif  numero==0:
    print("O numero é neutro")
else:
    print("o numero é impar")