from def_banco import pessoas

#===============================================
#Laboratório
#================================================

def analisar_sangue():
    print("\n================================")
    print("          LABORATÓRIO")
    print("==================================")

    cpf = input("Informe o CPF do doador: ")

    #Procurando doador
    for pessoa in pessoas:
        if pessoa.cpf == cpf:

            #verificando se houve coleta
            if pessoa.status_coleta != "Coleta realizada":
                print("\nO doador ainda não realizou a coleta.")
                return

            #mostrando dados do doador
            print("\n================================")
            print("       DOADOR ENCONTRADO")
            print("==================================")
            print(f"Nome: {pessoa.nome}")
            print(f"CPF: {pessoa.cpf}")
            print(f"Tipo sanguineo: {pessoa.tipo_sanguineo}")
            print(f"Data coletada: {pessoa.data_coleta}")
            print(f"Quantidade coletada: {pessoa.quantidade_coletada} ml")
            print(f"Status da coleta: {pessoa.status_coleta}")
            print("==================================")

            #resultado do laboratorio
            print("\nRESULTADO DO LABORATÓRIO")
            print("1 - Aprovado")
            print("2 - Reprovado")

            resultado = input("Informe o resultado: ")

            if resultado == "1":
                resultado_laboratorio = "Aprovado"

            elif resultado == "2":
                resultado_laboratorio = "Reprovado"

            else:
                print("Opção inválida.")
                return

            #Salvando os dados
            pessoa.resultado_laboratorio = resultado_laboratorio
            pessoa.status_laboratorio = "Análiese concluída"

            # Mostrando resultado
            print("\n================================")
            print("     ANÁLISE CONCLUÍDA!")
            print("==================================")
            print(f"Nome: {pessoa.nome}")
            print(f"CPF: {pessoa.cpf}")
            print(f"Resultado: {pessoa.resultado_laboratorio}")
            print(f"Status: {pessoa.status_laboratorio}")
            print("==================================")

            return

    print("\nCPF não encontrado.")