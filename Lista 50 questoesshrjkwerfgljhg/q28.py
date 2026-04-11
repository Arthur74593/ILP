# 28. Leia dois números inteiros. Se a soma deles for maior que 100, 
# exiba "Soma grande"; caso contrário, exiba "Soma pequena".
n1 = int(input("digite um numero:"))
n2 = int(input("digite outro numero:"))
soma = (n1+n2)
if soma>100:
    print("Soma grande")
elif soma==100:
    print("Soma igual a 100")
else:
    print("Soma pequena")