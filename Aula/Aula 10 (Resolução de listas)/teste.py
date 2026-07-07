from tabulate import tabulate 

dados = []
c = 0

while c <= 100:
    f = (c * 1.8) + 32
    k = c + 273.15
    
    if c < 15:
        classificação = 'fria'
    elif c <= 25:
        classificação = 'agradável'
    else:
        classificação = 'quente'

    dados.append([c, f, k, classificação])

    c += 10
print(tabulate(dados, headers=['Celsius', 'Fahrenheit', 'Kelvin', 'Classificação'], tablefmt ='grid'))