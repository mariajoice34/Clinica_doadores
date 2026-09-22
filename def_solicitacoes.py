from def_banco import pessoas

#==============================================
# SOLICITAÇÕES
#==============================================

def solicitar_sangue():
    print("\n================================")
    print("       SOLICITAÇÃO DE SANGUE")
    print("==================================")

    
    tipo_sanguineo = input("Informe o tipo sanguineo solicitado: ")

    quantidade = input("Informe a quantidade necessária (ml): ")

    motivo = input("Informe o motivo da solicitação: ")

    print("\n================================")
    print("   SOLICITAÇÃO REGISTRADA!")
    print("==================================")
    print(f"Tipo sanguíneo: {tipo_sanguineo}")
    print(f"Quantidade: {quantidade} ml")
    print(f"Motivo: {motivo}")
    print("Status: Pendente")
    print("==================================")
