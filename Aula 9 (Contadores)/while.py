# Programa de contagem com while
# Ele funciona para:
# - valor inicial menor que o final (crescente)
# - valor inicial maior que o final (decrescente)
# - valores iguais (executa uma vez)

# pede os valores ao usuário
valor_inicial = int(input("Digite o valor inicial: "))
valor_final = int(input("Digite o valor final: "))

# começa o contador com o valor inicial
contador = valor_inicial

# verifica se vai contar para cima
if valor_inicial < valor_final:
    # enquanto o contador for menor ou igual ao final
    while contador <= valor_final:
        print(contador)
        contador += 1  # soma 1 a cada repetição

# verifica se vai contar para baixo
elif valor_inicial > valor_final:
    # enquanto o contador for maior ou igual ao final
    while contador >= valor_final:
        print(contador)
        contador -= 1  # diminui 1 a cada repetição

# caso os valores sejam iguais
else:
    print("Os valores são iguais:")
    print(contador)