# 35. Leia a velocidade de um carro e exiba a multa correspondente:
# Velocidade ≤ 80 km/h: "Sem multa"
# Velocidade ≤ 100 km/h: "Multa leve: R$ 130"
# Velocidade ≤ 120 km/h: "Multa média: R$ 195"
# Velocidade > 120 km/h: "Multa grave: R$ 293 + suspensão"

velocidade = float(input("Digite a velocidade do carro:"))

if velocidade <= 80:
    print("Sem multa")
elif velocidade<= 100:
    print("Multa leve: R$130")
elif velocidade<=120:
    print("Multa média: R$195")
else:
    print("Multa grave: R$293 + sunspensão")