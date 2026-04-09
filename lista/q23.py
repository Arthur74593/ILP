A = 4
B = 10
C = 4
D = True
D2 = False
E = False
F = 0
G = -3
I = [1, 2, 3, 4, 5]

# REGRA DO AND
# Se o primeiro valor for False, ele retorna o primeiro
# Se o primeiro valor for True, ele retorna o segundo


# REGRA DO OR
# Se o primeiro valor for True, ele retorna o primeiro
# Se o primeiro valor for False, ele retorna o segundo

# D IGUAL A TRUE
print(D and B or A)
#  vai ficar (True and 10 or 4) e o entre o 10 e o 4 ,como esta com o or, o primeiro valor true (10) é retornado.
# e aparece 10 no terminal pois ,pela regra do and, se o primeiro for true o segundo, no caso 10, é retornado.

# D IGUAL A FALSE
print(D2 and B or A)
# entre false e 10 o false é escolhido e entre false e 4 o 4 é escolhido


