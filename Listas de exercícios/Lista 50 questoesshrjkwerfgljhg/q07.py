# 7. Leia o nome de um usuário. Se o nome tiver mais de 10 caracteres, exiba "Nome muito longo".
nome = input(f"Digite seu  nome:")
tamanho = len(nome)

if tamanho>10:
    print("Nome muito longo")