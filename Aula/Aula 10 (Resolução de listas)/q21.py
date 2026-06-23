# 21. Escreva um programa que lê n notas de alunos (onde n é fornecido pelo usuário) e exibe a maior nota lida.
n = int(input("Digite a quantidade de notas: "))

maior_nota = float('-inf')  # começa bem baixo

for i in range(n):
    nota = float(input("Digite a nota: "))
    
    if nota > maior_nota:
        maior_nota = nota

print(f"A maior nota é {maior_nota}")