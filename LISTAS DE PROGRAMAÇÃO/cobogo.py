lista = list(map(int, input("Digite os números separados por espaço: ").split()))

contagem = {}

for num in lista:
    if num in contagem:
        contagem[num] += 1
    else:
        contagem[num] = 1

menor_freq = float('inf')  
menos_repete = None

for num in contagem:
    if contagem[num] < menor_freq:
        menor_freq = contagem[num]
        menos_repete = num
    elif contagem[num] == menor_freq:
        if menos_repete is None or num < menos_repete:
            menos_repete = num

print(menos_repete)