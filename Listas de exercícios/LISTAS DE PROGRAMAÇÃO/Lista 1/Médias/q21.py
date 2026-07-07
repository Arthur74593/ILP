numero = int(input("Quantidade de números na lista:"))
lista = list(map(int, input("Digite o números separados por espaço:").split()))

contagem = {}

for num in lista:
    if num in contagem:
        contagem[num] += 1
    else:
        contagem[num] = 1

maior_frequencia = 0 

moda = None

for num in contagem:
    if  contagem[num] > maior_frequencia:
        maior_frequencia = contagem[num]
        moda = num
    elif contagem[num] == maior_frequencia:
        if moda is None or num < moda:
            moda = num

print(moda)