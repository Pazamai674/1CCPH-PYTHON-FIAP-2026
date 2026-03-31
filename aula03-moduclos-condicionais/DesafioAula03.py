idade_do_usuario = int(input('Digite sua idade: '))

Voto_Legivel_NO = 16
Voto_Ilegivel = 15
Voto_Obrigatorio = 18
Voto_L_N_Obrigatorio = 70

if idade_do_usuario <= Voto_Ilegivel:
    print("Voto Inelegível")
elif idade_do_usuario >= Voto_Obrigatorio and idade_do_usuario < Voto_L_N_Obrigatorio:
    print("Voto Obrigatório")
else:
    print("Voto Opcional / Legível Não Obrigatório")
