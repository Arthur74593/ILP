n = int(input("quantidade de valores a serem lidos:"))
lista = []
acima = 0

for i in range(n):
    num = int(input("Digite o valor:"))
    lista.append(num)
    soma = sum(lista)
    media = soma/n
if num > media:
    acima += 1 
    

print(acima)
print(media)
print(lista)