numero = int(input("Quantidade de números na lista"))
lista = list(map(int, input("Digite o números separados por espaço:").split()))

qtd_maior_media = 0
soma = 0
qtd = len(lista)

for num in lista:
    soma += num
    media = soma / qtd
if num > media:
    qtd_maior_media += 1

print(qtd_maior_media)