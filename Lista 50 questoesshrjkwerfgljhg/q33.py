# 33. Leia um número inteiro de 1 a 7 representando um dia da 
# semana e exiba o nome do dia correspondente (1 = Segunda, 2 = Terça, …, 7 = Domingo). 
# Se o valor estiver fora do intervalo, exiba "Dia inválido".

dia = int(input("Digite o dia da semnana:"))

if 1 <= dia <= 7:
    if dia==1:
        print("Domingo")
    elif dia==2:
        print("Segunda")
    elif dia==3:
        print("terça")
    elif dia==4:
        print("Quarta")
    elif dia==5:
        print("Quinta")
    elif dia==6:
        print("Sexta")
    elif dia==7:
        print("Sábado")
else:
    print("Dia inválido")