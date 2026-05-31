n = int(input("Quantidade de números na lista:"))
lista_a = list(map(int, input("Digite o números separados por espaço:").split()))
m = int(input("Quantidade de números na lista:"))
lista_b = list(map(int, input("Digite o números separados por espaço:").split()))
diferenca  = []

for num in lista_a:
    if num not in lista_b and num not in diferenca:
        diferenca.append(num)
print(*diferenca)