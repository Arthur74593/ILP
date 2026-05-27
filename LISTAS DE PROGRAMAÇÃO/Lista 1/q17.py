n = int(input("Digite o tamanho de A: "))
a = []
for i in range(n):
    x = int(input(f"Digite o elemento {i+1} de A: "))
    a.append(x)

m = int(input("Digite o tamanho de B: "))
b = []
for i in range(m):
    x = int(input(f"Digite o elemento {i+1} de B: "))
    b.append(x)

resultado = []

for x in a:
    esta_em_b = False
    for y in b:
        if x == y:
            esta_em_b = True
            break
    
    if not esta_em_b and x not in resultado:
        resultado.append(x)

if resultado:
    for x in resultado:
        print(x, end=" ")
else:
    print("VAZIA")