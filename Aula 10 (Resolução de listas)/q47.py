# 47. Escreva um programa que simula um jogo de adivinhação: o programa sorteia um número inteiro entre 1 e 100 e o usuário tenta adivinhar. 
# A cada tentativa o programa informa se o chute foi "muito baixo", "muito alto" ou "acertou!". O laço termina quando o usuário acertar.

# Dica: use import random e random.randint(1, 100) para sortear o número.

import random
cleiton = random.randint(1,100)
chute = 0

while cleiton != chute:
    chute = int(input("Digite o seu chute:"))
    if chute < cleiton:
        print("muito baixo")
    elif chute > cleiton:
        print("Muito alto")
    else:
        print("Acertou galadinho!!")
    



