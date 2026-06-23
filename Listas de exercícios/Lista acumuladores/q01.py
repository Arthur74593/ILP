# Leia um número inteiro positivo N. Imprima todos os números de N até 1 em ordem decrescente, um por linha. Ao final, imprima Fogo!.

# Exemplo:

# Entrada: 5
# Saída: 5 4 3 2 1 Fogo!

n = int(input("Digite o começo da contagem:"))

for i in range(n, -1, -1):
    print(i)
    if i ==0:
        print("Fogo!")
    

