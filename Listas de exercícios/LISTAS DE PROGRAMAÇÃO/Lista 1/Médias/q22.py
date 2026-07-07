n = int(input())
numeros = list(map(int, input().split()))

valores_distintos = sorted(set(numeros), reverse=True)

if len(valores_distintos) >= 2:
    print(valores_distintos[1])
else:
    print("NÃO EXISTE")