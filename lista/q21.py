A = 4
B = 10
C = 4
D = True
E = False
F = 0
G = -3
I = [1, 2, 3, 4, 5]

A and B
E and A
D or B
E or A

# REGRA DO AND
# Se o primeiro valor for False, ele retorna o primeiro
# Se o primeiro valor for True, ele retorna o segundo


# REGRA DO OR
# Se o primeiro valor for True, ele retorna o primeiro
# Se o primeiro valor for False, ele retorna o segundo

print( A and B)
# retornara 10 por que quando o primeiro valor é true (diferente de 0) o segundo 
# numero sai no terminal
print( E and A)
# retornou false pois se o  primeiro termo for "false" (igual a 0) ele sai no terminal
print(D or B)
# retornou "true" pois o primeiro é "true"
print(E or A)
# retornou "4" pois o primeiro valor era "false" logo ele vai retornar o segundo