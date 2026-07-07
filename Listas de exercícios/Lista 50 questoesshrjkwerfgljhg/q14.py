# 14. Leia três notas de um aluno.
#  Calcule a média. Se a média for maior ou igual a
#  5 e menor que 7, exiba "Em recuperação".
n1 = float(input("Digite a  nota:"))
n2 = float(input("Digite outra nota:"))
n3 = float(input("Digite outra nota:"))
media = float(n1+n2+n3)/3
if 5<=media<7:
    print("Em recuperação")
else:
    print("Aprovado")