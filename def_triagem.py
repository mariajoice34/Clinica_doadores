from def_banco import pessoas

###########################################################
#Triagem
############################################################

def registrar_triagem():
    print("\n================================")
    print("           TRIAGEM")
    print("==================================")

    cpf = input("Informe o CPF do doador: ")

    #Procurar do doador 😭
    for pessoa in pessoas:
        if pessoa.cpf == cpf:

            print("\n================================")
            print("       DOADOR ENCONTRADO")
            print("==================================")
            print(f"Nome: {pessoa.nome}")
            print(f"CPF: {pessoa.cpf}")
            print(f"Tipo sanguineo: {pessoa.tipo_sanguineo}")
            print("==================================")

            #Pressão
            pressao = input("\nInforme a pressão arterial: ")

            #Hemoglobina
            hemoglobina = input("Informe o nivel de hemoglobina: ")

            #teste de doença
            print("\nTESTE DE DOENÇAS")
            print("1 - Negativa")
            print("2 - Positivo")

            teste = input("Informe o resultado dos testes: ")

            if teste == "1":
                teste_doencas = "Negativo"

            elif teste == "2":
                teste_doencas = "Positivo"

            else:
                print("Opção inválida.")
                return

            #salvando dados da triagem
            pessoa.pressao = pressao
            pessoa.hemoglobina = hemoglobina
            pessoa.testes_doencas = teste_doencas

            print("\n================================")
            print("     TRIAGEM REGISTRADA!")
            print("\n================================")
            print(f"Pressão arterial: {pessoa.pressao}")
            print(f"Hemoglobina: {pessoa.hemoglobina}")
            print(f"Testes de doenças: {pessoa.testes_doencas}")
            print("\n================================")

            return

        print("\nCPF não encontrado.")

#########################################################
#Aprovando doador
##########################################################

def aprovar_doador():
     print("\n================================")
     print("       APROVAR DOADOR")
     print("================================")

     cpf = input("Informe o CPF do doador: ")

     for pessoa in pessoas:
         
         if pessoa.cpf == cpf:
             
             if pessoa.pressao is None:
                 print("\n O doador não realizou a triagem.")
                 return

             if pessoa.testes_doencas == "Positivo":
                 print("\nDoador não pode ser aprovado.")
                 print("Resultado dos testes: Positivo")
                 return
                 
             pessoa.status_triagem = "Aprovado"

             print("\n================================")
             print("       DOADOR APROVADO")
             print("==================================")
             print(f"Nome: {pessoa.nome}")
             print(f"CPF: {pessoa.cpf}")
             print(f"Status: {pessoa.status_triagem}")
             print("==================================")
             return

print("\nCPF não encontrado. ")

###############################################################
#Reprovando doador
###############################################################

def reprovar_doador():
    print("\n================================")
    print("       REPROVAR DOADOR")
    print("==================================")

    cpf = input("Informe o CPF do doador: ")
    for pessoa in pessoas:

        if pessoa.cpf == cpf:
            if pessoa.pressao is None:
                print("\nO doador ainda não realizou a triagem.")
                return
            pessoa.status_triagem = "Reprovado"

            print("\n=================================")
            print("       DOADOR REPROVADO")
            print("===================================")
            print(f"Nome: {pessoa.nome}")
            print(f"CPF: {pessoa.cpf}")
            print(f"Status: {pessoa.status_triagem}")
            print("===================================")
            return
    print("\n CPF não encontrado.")


         
    

