# 22. Leia o salário de uma pessoa. Se o salário for maior que 3000,
#  calcule e exiba o imposto de 15%; caso contrário, calcule e exiba o imposto de 7.5%.
salario= float(input("digite seu salario:"))
imposto1= salario-(salario*0.15)
imposto2 = salario-(salario*0.075)

if salario>3000:
    print(f"Salario pos-impostos:{imposto1}")
else:
    print(f"Salario pos-impostos:{imposto2}")