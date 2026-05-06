print("C  F  K  Classificação")

for c in range(0, 101, 10):
    f = c * 9/5 + 32
    k = c + 273.15

    if c < 15:
        clas = "Fria"
    elif c <= 25:
        clas = "Agradável"
    else:
        clas = "Quente"

    print(f"{c:<3} {f:<5.1f} {k:<7.2f} {clas}")