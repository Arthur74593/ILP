# 38. Leia dois números e um operador (+, -, *, /). 
# Realize a operação correspondente e exiba o resultado. 
# Se o operador for / e o divisor for 0, exiba mensagem de erro. 
# Se o operador for inválido, exiba "Operador inválido".

n1 = float(input("Digite o número:"))
n2 = float(input("Digite outro número:"))
operador = input(f"Digite o operador(+,-,*,/):")

if operador=="+":
    print(n1+n2)
elif operador=="-":
    print(n1-n2)
elif operador=="*":
    print(n1*n2)
if operador=="/":
        print(n1/n2)
elif n2==0:
        print(ValueError("Não é possível dividir por zero"))
else:
    print("Operador inválido ")



