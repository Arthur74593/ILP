numero = int(input("Quantidade de números na lista:"))
lista = list(map(int, input("Digite o números separados por espaço:").split()))
lista_com_prefixos_acumulados = []
soma =  0

for num in lista:
    soma += num
    lista_com_prefixos_acumulados.append(soma)

print(*lista_com_prefixos_acumulados)
