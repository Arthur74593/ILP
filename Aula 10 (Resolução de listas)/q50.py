# 50. Escreva um programa que exibe a seguinte tabela de conversão
#  de temperaturas de 0 °C a 100 °C, de 10 em 10 graus, mostrando Celsius, Fahrenheit e Kelvin. 
# Ao lado de cada linha, classifique a temperatura como "fria" (< 15 °C), "agradável" (15 °C a 25 °C) 
# ou "quente" (> 25 °C).

# Celsius	Fahrenheit	Kelvin	Classificação
# 0	32.0	273.15	fria
# 10	50.0	283.15	fria
# ...	...	...	...
# Fórmulas: F = C × 9/5 + 32 ; K = C + 273.15

c = 0

print("Celsius Farenheit kelvin Classificação")

while c <100:
    c += 10
    f = c*9/5 + 32
    k = c + 273.15
    if c <15:
        clas = "Fria"
    elif c <= 25:
        clas = "Agradável"
    else:
        clas = "Quente"

    print(c,f,k,clas) 


