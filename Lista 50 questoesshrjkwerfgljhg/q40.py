# 40. Leia um caractere e informe se é:
# Uma vogal minúscula (a, e, i, o, u)
# Uma consoante minúscula (qualquer outra letra de a a z)
# Um dígito (0 a 9)
# Outro caractere

caractere = input("Digite um caratere:")

if len(caractere) != 1:
    print("Digite apenas um caractere")
else:
    if caractere in "aeiou":
        print("vogal minúscula")
    elif caractere >= "a" and caractere<= "z":
        print("Consoante minuscula")
    elif caractere >= '0' and caractere <= '9':
        print("Dígito")
    else:
        print("Outro caractere")