# Lóica E (and)

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entrar no programa")

#Lógica ou (or)
logica_ou = True or False or False
print(logica_ou)

#operação not
negacao = not False
print(negacao)

if not verifica_login:
    print("Seu login ou senha estao errados")