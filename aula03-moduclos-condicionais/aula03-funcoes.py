# fução com parametro sem retorno

def boas_vindas(nome):
    print(f"Bem vindo {nome}")

nome_digitado = input("Digite seu nome: ")
boas_vindas(nome_digitado)

#Funções com parametro com retorno

def soma(num_a,  num_b):
    soma = num_a + num_b
    return soma

resultando_soma = soma(10, 20)
print(resultando_soma)