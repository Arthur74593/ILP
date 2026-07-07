# 24. Leia dois números reais. Calcule e exiba a divisão do primeiro pelo segundo. 
# Se o segundo for zero, exiba "Divisão por zero não é permitida".
n1 = float(input("digite um numero:"))
n2 = float(input("digite outro numero:"))


if n2!=0 :
    print(n1/n2)
else:
    print("Divisão por zero não é permitida")