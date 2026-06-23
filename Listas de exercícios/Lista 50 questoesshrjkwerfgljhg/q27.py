# 27. Leia o ano de nascimento de uma pessoa. Se a pessoa tiver 65 anos ou mais em 2026, 
# exiba "Elegível para aposentadoria"; caso contrário, exiba "Não elegível ainda".
nascimento = int(input("Digite seu ano de nascimento:"))

if nascimento<=1961:
    print("Elegível para aposentadoria")
else:
    print("Não elegível ainda")