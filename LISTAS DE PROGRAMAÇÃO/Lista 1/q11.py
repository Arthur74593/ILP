n = int(input("quantidade de valores a serem lidos:"))
lista = []
quantos = 0

for i in range(n):
    num = int(input("Digite o valor:"))
    lista.append(num)
x =  int(input("Digite um valor que pode, ou não, estar na lista:"))
for i in range(n):
    if x in lista:
        quantos = lista.count(x)
    
print(quantos)
        