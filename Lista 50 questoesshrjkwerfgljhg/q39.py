# # 39. Leia o salário de um funcionário e calcule o reajuste:
# Salário ≤ 1500: reajuste de 15%
# Salário ≤ 3000: reajuste de 10%
# Salário ≤ 6000: reajuste de 7%
# Salário > 6000: reajuste de 3%
# Exiba o novo salário.

salario = float(input("Digite seu salário:"))

s1 = salario+(salario*0.15)
s2 = salario+(salario*0.10)
s3 = salario+(salario*0.07)
s4 = salario+(salario*0.03)

if salario <= 1500:
    print(f"Nvo osalário:{s1}")
elif salario <= 3000:
    print(f"Nvo osalário:{s2}")
elif salario<=6000:
    print(f"Nvo osalário:{s3}")
else:
    print(f"Nvo osalário:{s4}")
