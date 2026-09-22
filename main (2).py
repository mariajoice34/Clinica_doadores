import def_recepcao
import def_triagem
import def_coleta
import def_laboratio
import def_estoque
import def_solicitacoes



# ============================================================
# SUBMENU RECEPÇÃO
# ============================================================
def sub_menu1():

    while True:

        print("\n================================")
        print("          RECEPÇÃO")
        print("================================")
        print("1 - Verificar doador")
        print("2 - Cadastrar doador")
        print("3 - Consultar histórico")
        print("4 - Voltar")

        opcao = int(input("Escolha: "))

        match opcao:

            case 1:
                def_recepcao.verificar_doador()

            case 2:
                def_recepcao.cadastro_recepcao()

            case 3:
               def_recepcao.consultar_historico()

            case 4:
                return

            case _:
                print("Opção inválida")

# ============================================================
# SUBMENU TRIAGEM
# ============================================================

def sub_menu_triagem():
    while True:
         print("\n================================")
         print("           TRIAGEM")
         print("==================================")
         print("1 - Registrar triagem")
         print("2 - Aprovar doador")
         print("3 - Reprovar doador")
         print("4 - Voltar")

         opcao = int(input("Escolha: "))

         match opcao:

            case 1:
                def_triagem.registrar_triagem()

            case 2:
                def_triagem.aprovar_doador()

            case 3:
                def_triagem.reprovar_doador()

            case 4:
                return

            case _:
                print("Opção inválida")


#============================================================
# SUBMENU ESTOQUE
#============================================================

def sub_menu_estoque():

    while True:
        print("\n================================")
        print("           ESTOQUE")
        print("==================================")
        print("1 - Entrada no estoque")
        print("2 - Consultar estoque")
        print("3 - Saída do estoque")
        print("4 - Voltar")

        opcao = int(input("Escolha: "))

        match opcao:
            case 1:
                def_estoque.entrada_estoque()

            case 2:
                def_estoque.consultar_estoque()

            case 3:
                def_estoque.saida_estoque()
            
            case 4:
                return

            case _:
                print("Opção inválida")


# ============================================================
# MENU PRINCIPAL
# ============================================================

while True:

    print("\n================================")
    print("        MENU PRINCIPAL")
    print("================================")
    print("1 - Recepção")
    print("2 - Triagem")
    print("3 - Coleta de sangue")
    print("4 - Laboratório")
    print("5 - Estoque")
    print("6 - Solicitações")
    print("7 - Sair")
    print("================================")
    escolha = int(input("Escolha: "))

    match escolha:
        case 1:
            sub_menu1()

        case 2:
            sub_menu_triagem()

        case 3:
            def_coleta.registra_coleta()

        case 4:
            def_laboratio.analisar_sangue()

        case 5:
            sub_menu_estoque()

        case 6:
            def_solicitacoes.solicitar_sangue()
        case 7:
            print("\nSaindo...")
            break

        case _:
            print("\nOpção inválida")