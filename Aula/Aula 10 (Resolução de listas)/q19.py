# 19. Escreva um programa que imprime os primeiros n termos da progressão aritmética com primeiro termo a e razão r, onde n, a e r são fornecidos pelo usuário.
a = float(input("Digite o primeiro termo da p.a:"))
r = float(input("DIgite a razão da p.a:"))
n = int(input("Digite de termos a serem impressos:"))


for i in range(n):
    print(a)
    a+= r

