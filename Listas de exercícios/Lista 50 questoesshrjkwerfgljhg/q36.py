# #36. Leia a idade de uma pessoa e exiba a categoria:
# Idade < 12: "Criança"
# Idade < 18: "Adolescente"
# Idade < 60: "Adulto"
# Idade ≥ 60: "Idoso"

idade = int(input("Digite dua idade:"))

if idade <12:
    print("Criança")
elif idade <18:
    print("Adolescente")
elif idade <60:
    print("Adulto")
else:
    print("Idoso")