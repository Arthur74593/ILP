n = int(input("Quantidade de números a serem lidos:"))
lista = []

for i in range(n):
    num = int(input(f'valor:'))
    lista.append(num)
    maior = max(lista)
    menor = min(lista)

print(f"{menor} {maior}")
