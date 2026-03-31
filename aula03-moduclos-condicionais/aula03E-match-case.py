escolha_usuario = 1
# 0 -> sair do programa
# 1 -> entrar o programa
# >>>> erro!

match escolha_usuario:
    case 0:
        print("Sair o programa")
    case 1:
        print("Entar no programa")
    case _:
            print("Erro")