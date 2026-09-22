from def_banco import pessoas

#==============================================
#Coleta de sangue
#==============================================

def registra_coleta():
    print("\n================================")
    print("           COLETA DE SANGUE")
    print("==================================")

    cpf = input("Informe o CPF do doador: ")

    #procurar doador
    for pessoa in pessoas:
        if pessoa.cpf == cpf:

            #verificando se o doador foi aprovado
            if pessoa.status_triagem != "Aprovado":
                print("\nO doador não foi aprovado na triagem.")
                return

            #Mostrando dados do doador
            print("\n================================")
            print("       DOADOR ENCONTRADO")
            print("==================================")
            print(f"Nome: {pessoa.nome}")  
            print(f"CPF: {pessoa.cpf}")
            print(f"Tipo sanguineo: {pessoa.tipo_sanguineo}")
            print(f"Status da triagem: {pessoa.status_triagem}")
            print("==================================")

            data_coleta = input("\nInforme a data de coleta (DD/MM/AAAA): ")

            quantidade = input("Informe a quantidade coletada (ml): ")

            #salvando os dados da coleta
            pessoa.data_coleta = data_coleta
            pessoa.quantidade_coletada = quantidade
            pessoa.status_coleta = "Coleta realizada"

            # Mostrando resultado
            print("\n================================")
            print("       COLETA REGISTRADA!")
            print("==================================")
            print(f"Nome: {pessoa.nome}")
            print(f"CPF: {pessoa.cpf}")
            print(f"Data da coleta: {pessoa.data_coleta}")
            print(f"Quantidade coletada: {pessoa.quantidade_coletada} ml")
            print(f"Status da coleta: {pessoa.status_coleta}")
            print("==================================")

            return
    print("\nCPF não encontrado.")
