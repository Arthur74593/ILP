# 29. Leia o peso e a altura de uma pessoa e calcule o IMC (peso / altura²). 
# Se o IMC for menor que 25, exiba "Peso normal"; caso contrário, exiba "Acima do peso".
peso = float(input("Digite seu peso(em KG):"))
altura = float(input("DIgite sua altura(EM m):"))
imc = float(peso)/altura**2
if imc<25:
    print("peso normal")
else:
    print("Acima do peso")