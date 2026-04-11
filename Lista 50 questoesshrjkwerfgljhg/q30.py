# 30. Leia uma string. Se ela tiver mais de 5 caracteres, 
# exiba a string em maiúsculas; caso contrário, exiba-a em minúsculas.
string  = input("Digite uma frase:")
tamanho = len(string)

if tamanho>5:
    print(string.upper())  
else:
    print(string.lower())
