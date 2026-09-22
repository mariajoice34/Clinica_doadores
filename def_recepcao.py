import datetime


from def_banco import Pessoas, pessoas


def cadastro_recepcao():
# ============================================================
# SEXO
# ============================================================
    
    while True:
        print("\nINFORME SEU SEXO:")
        print("1 - Masculino")
        print("2 - Feminino")

        escolha = input("Insira sua escolha: ")

        if escolha == "1":
            sexo = "Masculino"
            break

        elif escolha == "2":
            sexo = "Feminino"
            break

        else:
            print("ERRO! escolha invalida")
            continue

# ============================================================
# CPF
# ============================================================
    
    while True:
            
            cpf = input("Digite um cpf: ")

            if not cpf:
                print("ERRO! insira um cpf")
                continue

            elif len(cpf) != 11 or not cpf.isnumeric():
                print("ERRO! insira um cpf válido com 11 números.")
                continue

            else:
                break

# ============================================================
# NOME
# ============================================================
    
    while True:
        nome=input("\nDigite um nome: ")

        if not nome:
            print("ERRO! insira um nome")
            continue

        elif len(nome) < 3:
            print("ERRO! insira um nome válido.")
            continue

        elif nome.isnumeric():
            print("ERRO! insira um nome válido.")
            continue

        else:
            break

# ============================================================
# DATA DE NASCIMENTO
# ============================================================
    
    while True:
        data = input("\nOBS:DD/MM/AAAA"
                   "\nDigite sua data de nascimento: ")

        try:
            data = datetime.datetime.strptime(data, "%d/%m/%Y")
            break

        except ValueError:
            print("Data inválida. Use DD/MM/AAAA")

# ============================================================
# TIPO SANGUÍNEO
# ============================================================

    while True:
        print("\n INFORME SEU TIPO SANGUINEO: ")
        print("1 - A+")
        print("2 - A-")
        print("3 - B+")
        print("4 - B-")
        print("5 - AB+")
        print("6 - AB-")
        print("7 - O+")
        print("8 - O-")

        tipo = input("Insira sua escolha: ")

        tipos = {
            "1": "A+",
            "2": "A-",
            "3": "B+",
            "4": "B-",
            "5": "AB+",
            "6": "AB-",
            "7": "O+",
            "8": "O-"
        }

        if tipo in tipos:
            tipo_sanguineo = tipos[tipo]
            break

        else:
            print("ERRO! Escolha inválida.")

# ============================================================
# ENDEREÇO
# ============================================================

    while True:
        endereco = input("informe seu endereço: ")

        if not endereco:
            print("ERRO!informe seu endereço")
            continue

        elif len(endereco) < 10:
            print("Informe um endereço válido")
            continue

        else:
            break

# ============================================================
# TELEFONE
# ============================================================
    while True:
        telefone = input("\nInforme seu telefone: ")

        if not telefone:
            print("ERRO!informe seu telefone")
            continue

        elif len(telefone) != 11:
            print("ERRO!informe um numero de telefone válido com 11 números.")
            continue

        elif not telefone.isdigit():
            print("Digite apenas números")
            continue

        else:
           break
# ============================================================
# CRIANDO A NOVA PESSOA
# ============================================================

    nova_pessoa = Pessoas (
        cpf,
        nome,
        data,
        sexo,
        tipo_sanguineo,
        endereco,
        telefone
    )

    pessoas.append(nova_pessoa)

    print("\n================================")
    print("     CADASTRO REALIZADO!")
    print("==================================")

    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    print(f"Sexo: {sexo}")
    print(f"Tipo sanguineo: {tipo_sanguineo}")
    print("==================================")


def verificar_doador():
    cpf = (input("informe o cpf do doador: "))

    for pessoa in pessoas:

        if pessoa.cpf == cpf:
            print("\n================================")
            print("       DOADOR ENCONTRADO")
            print("================================")
            print(f"nome: {pessoa.nome}")
            print(f"CPF: {pessoa.cpf}")
            print(f"Sexo: {pessoa.sexo}")
            print(f"Tipo sanguineo: {pessoa.tipo_sanguineo}")
            print(f"Data de nascimento: {pessoa.data.strftime("%d/%m/%Y")}")
            print(f"Endereço: {pessoa.endereco}")
            print(f"Telefone: {pessoa.telefone}")
            print("\n================================")
            
            return pessoa

    print("CPF não encontrado")
    return None

def consultar_historico():

    print("\n================================")
    print("       HISTÓRICO DE DOAÇÕES")
    print("================================")

    # Ainda será desenvolvido
    print("Função ainda não implementada.")






