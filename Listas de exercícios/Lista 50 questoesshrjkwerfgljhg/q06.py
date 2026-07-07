# 6. Leia um número real que representa a temperatura em graus Celsius. 
# Se a temperatura for maior que 37.5, exiba "Febre detectada".

temperatura = float(input("Digite sua temperatura(em celsius):"))

if temperatura>37.5:
    print("Febre detectada")
else:
    print("Sem febre")