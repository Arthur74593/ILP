n = int(input("quantidade de valores a serem lidos:"))
lista = []

for i in range(n):
    num = int(input("Digite o valor:"))
    lista.append(num)

x =  int(input("Digite um valor que pode, ou não, estar na lista:"))
 
if x in lista:
    posicao = lista.index(x)
    print(posicao)
else:
    print("-1")