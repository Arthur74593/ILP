numero = int(input("Quantidade de números na lista:"))
lista = list(map(int, input("Digite o números separados por espaço:").split()))
x = int(input("Digite um número que pode , ou não, estar na lista:"))
qtd = 0

for num in lista:
    if num == x:
        qtd += 1

print(qtd)

        
