from def_banco import pessoas

#==============================================
# ESTOQUE
#==============================================

def entrada_estoque():
    print("\n================================")
    print("       ENTRADA NO ESTOQUE")
    print("==================================")

    cpf = input("Informe o CPF do doador: ")

    #Procurando doador 
    for pessoa in pessoas:

        if pessoa.cpf == cpf:

            #verificar se o laboratorio aprovou
            if pessoa.status_laboratorio != "Análiese concluída":
                print("\nA análise do laboratório ainda não foi concluída.")
                return

            if pessoa.resultado_laboratorio != "Aprovado":
                print("\nO sangue foi reprovado pelo laboratório.")
                return

            #salavndo no estoque
            pessoa.status_estoque = "Disponivel"

            print("\n================================")
            print("      SANGUE ADICIONADO!")
            print("==================================")
            print(f"Nome: {pessoa.nome}")
            print(f"CPF: {pessoa.cpf}")
            print(f"Tipo sanguineo: {pessoa.tipo_sanguineo}")
            print(f"Quantidade: {pessoa.quantidade_coletada} ml")
            print(f"Status: {pessoa.status_estoque}")
            print("==================================")

            return
    print("\nCPF não encontrado.")

#==============================================
# CONSULTAR ESTOQUE
#==============================================

def consultar_estoque():
    print("\n================================")
    print("       ESTOQUE DE SANGUE")
    print("==================================")

    encontrou = False

    for pessoa in pessoas:

        if pessoa.status_estoque == "Disponivel":
            encontrou = True

            print("\n--------------------------------")
            print(f"Nome: {pessoa.nome}")
            print(f"CPF: {pessoa.cpf}")
            print(f"Tipo sanguineo: {pessoa.tipo_sanguineo}")
            print(f"Quantidade: {pessoa.quantidade_coletada} ml")
            print(f"Status: {pessoa.status_estoque}")
            print("--------------------------------")

    if not encontrou:
        print("\nNão existem bolsas disponíveis no estoque.")

#==============================================
# SAÍDA DO ESTOQUE
#==============================================

def saida_estoque():
    print("\n================================")
    print("        SAÍDA DO ESTOQUE")
    print("==================================")

    cpf = input("Informe o CPF do doador: ")

    for pessoa in pessoas:

        if pessoa.cpf == cpf:
            if pessoa.status_estoque != "Disponivel":
                print("\nEsta bolsa não está disponivel no estoque.")
                return
            pessoa.status_estoque = "Utilizado"

            print("\n================================")
            print("       SAÍDA REGISTRADA!")
            print("==================================")
            print(f"Nome: {pessoa.nome}")
            print(f"CPF: {pessoa.cpf}")
            print(f"Tipo sanguineo: {pessoa.tipo_sanguineo}")
            print(f"Quantidade: {pessoa.quantidade_coletada} ml")
            print(f"Status: {pessoa.status_estoque}")
            print("==================================")

            return
    print("\nCPF não encontrado.")
    
