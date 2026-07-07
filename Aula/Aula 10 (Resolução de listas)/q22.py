#  22. Escreva um programa que lê n notas de alunos (onde n é fornec#ido pelo usuário) e exibe a menor nota lida.
n = int(input("Digite a quantidade de notas: "))

menor_nota = float('inf') 

for i in range(n):
    nota = float(input("Digite a nota: "))
    
    if nota < menor_nota:
        menor_nota = nota

print(f"A menor nota é {menor_nota}")   