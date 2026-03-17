print("ola mundo")

print(7 + 4)
print("7+ 4")
print("7" + "4") # cncatenando strings

# comentarios em python (1 linha)
'''
    comentarios
    multiplas
    linhas
'''

# variaveis
nome =  "Pedro" #str
idade = 18 #int
peso = 50.3 #float

print(nome, idade, peso)

#input simula forms no prompt

nome = input("Qual o seu nome?")
idade = input("Qual a sua idade?")
peso = input("Qual o seu peso?")

print(nome, idade, peso)
print(f"oiii,{nome}!!!")

ano_nascimento = 2007
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(idade)