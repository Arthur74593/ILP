# 16. Escreva um programa que lê números reais do usuário enquanto o usuário não
#  digitar um número negativo, e ao final exibe a soma de todos os valores lidos 
# (sem incluir o negativo).

num = float(input("Digite um número:"))
soma = 0


while num >= 0: 
    soma += num
    num = float(input("Digite um número:"))
    

print(f'A soma dos números é:{soma}')

