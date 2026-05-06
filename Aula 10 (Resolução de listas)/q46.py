# 46. Escreva um programa que lê n números reais e classifica cada um como:

# "pequeno" se o valor for menor que 10,
# "médio" se o valor estiver entre 10 e 100 (inclusive),
# "grande" se o valor for maior que 100.
# Ao final, exibe a contagem de cada categoria.

n = int(input("Digite a quantidade de numeros que voce quer ler:"))
soma_pequeno = 0
soma_medio = 0
soma_grande = 0

for i in range(1,n+1):
    if i < 10:
        soma_pequeno += 1
    elif i < 100:
        soma_medio += 1
    else:
        soma_grande += 1
print(f'Soma pequeno:{soma_pequeno}')
print(f'Soma media:{soma_medio}')
print(f'Soma grande:{soma_grande}')
# kcjsdhvrsgv


