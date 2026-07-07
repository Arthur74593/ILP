# Leia um número inteiro N (1 ≤ N ≤ 10). Imprima a tabuada de multiplicação de N, do 1 ao 10, no formato N x i = resultado.
# Exemplo (N=3):

n = int(input("Digite um numero:"))

if 1 <= n <= 10:
    for i in range(1,11):
        print(n*i)

