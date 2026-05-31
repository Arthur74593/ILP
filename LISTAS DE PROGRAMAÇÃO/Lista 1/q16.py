n = int(input("Quantidade de números na lista:"))
lista_a = list(map(int, input("Digite o números separados por espaço:").split()))
m = int(input("Quantidade de números na lista:"))
lista_b = list(map(int, input("Digite o números separados por espaço:").split()))
intersecao  =[]

for num in lista_a:
    if num in lista_b and num not  in intersecao:
        intersecao.append(num)
print(*intersecao)