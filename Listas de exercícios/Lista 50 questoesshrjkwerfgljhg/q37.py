# 37. Leia o mês (1 a 12) e exiba a estação do ano correspondente no hemisfério sul:
# Meses 12, 1, 2: "Verão"
# Meses 3, 4, 5: "Outono"
# Meses 6, 7, 8: "Inverno"
# Meses 9, 10, 11: "Primavera"
# Valor fora do intervalo: "Mês inválido"

mes = int(input("Digite o mes do ano:"))

if mes in [12,1,2]:
    print("Verão")
elif mes in[3,4,5]:
    print("Outono")
elif mes in [6,7,8]:
    print("Inverno")
elif mes in [9,10,11]:
    print("Primavera")
else:
    print("Mês inválido")
    