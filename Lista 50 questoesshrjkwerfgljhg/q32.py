# 32. Leia a nota de um aluno (0 a 10) e exiba o conceito:
# Nota ≥ 9: "A"
# Nota ≥ 7: "B"
# Nota ≥ 5: "C"
# Nota < 5: "D"

nota = float(input("digite sua nota(0 a 10):"))

if  0 >= nota >=10:
    if nota >=9:
        print("Voce  tirou  um A")
    elif nota >=7:
        print("Voce  tirou  um B")
    elif nota >=5:
        print("Voce  tirou  um C")
    else:
        print("Voce  tirou  um D")
else:
    print("O numero esta fora do intervalo")
        

