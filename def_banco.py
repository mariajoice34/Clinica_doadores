# vou simular o banco de dados com dicionario,dps vc so substitui pelo o banco que você quer



class Pessoas():
    def __init__(self, cpf, nome, data, sexo, tipo_sanguineo, endereco, telefone):
        self.cpf = cpf
        self.nome = nome
        self.data = data
        self.sexo = sexo
        self.tipo_sanguineo = tipo_sanguineo
        self.endereco = endereco
        self.telefone = telefone

        #dados da triagem
        self.pressao = None
        self.hemoglobina = None
        self.testes_doencas = None
        self.status_triagem = None

        #dados da coleta
        self.data_coleta = None
        self.quantidade_coletada = None
        self.status_coleta= None

        #dados do laboratio
        self.resultado_laboratorio = None
        self.status_laboratorio = None

        #dados do estoque
        self.status_estoque = None



pessoas = []

