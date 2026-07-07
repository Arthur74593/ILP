# 23. Leia uma senha digitada pelo usuário. Compare com a senha "python2026". 
# Se for correta, exiba "Acesso permitido"; caso contrário, exiba "Acesso negado".
senhadigitada = input("Digite sua senha:")
senhacerta = ("python2026")
if senhadigitada==senhacerta:
    print("Acesso liberado")
else:
    print("Acesso negado")