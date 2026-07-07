# 34. Leia o IMC de uma pessoa e classifique:
# IMC < 18.5: "Abaixo do peso"
# IMC < 25: "Peso normal"
# IMC < 30: "Sobrepeso"
# IMC ≥ 30: "Obesidade"

peso= float(input("Digite seu peso(kg):"))
altura= float(input("Digite sua alltura(m):"))
imc = (peso)/ (altura**2)

if imc< 18.5:
    print("Abaixo do peso")
elif imc<25:
    print("Peso normal")
elif imc<30:
    print("Sobrepeso")
else:
    print("Obesidade")


print(f"Seu IMC é igual a:{imc}")
