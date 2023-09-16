class Bacen:
    def __init__(self):
        self.listaDeBancos: []

class Cliente:

    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        

class Banco:
    listasDeMalPagadores = []
    def __init__(self, nomeConstrutor):
        self.nome = nomeConstrutor
        self.descricao = ''
        self.id = 0
        self.listaDeCliente = []

    def criarCliente(self ,nome ,senha):
        cliente = Cliente(nome, senha)
        # cliente.nome = nome
        # cliente.senha = senha
        self.listaDeCliente.append(cliente)

    def addMalPagador(self ,nome ,senha):
        cliente = Cliente(nome, senha)
        cliente.nome = nome
        cliente.senha = senha
        self.listaDeCliente.append(cliente)


    def imprimirListaCliente(self):
        for clienteIndex in range(0,len(self.listaDeCliente)):
            print('index:', clienteIndex +1 ,'-',self.listaDeCliente[clienteIndex].nome, "saldo:", self.listaDeCliente[clienteIndex].saldo)

    def imprimirListaDeMalPagadores(self):
        for clienteIndex in range(0,len(self.listasDeMalPagadores)):
            print('index:', clienteIndex +1 ,'-',self.listasDeMalPagadores[clienteIndex].nome)

    
    def deposito(self, nome, valor):
        index = -1
        for cliente in self.listaDeCliente:
            if cliente.nome == nome:
                cliente.saldo += valor
            break



def localizarBanco(nome):
    for banco in listaDeBanco:
        if banco.nome == nome:
            return banco
        break
    return -1



## Codigo Fonte Main

listaDeBanco = []
flagBacen = True

while(True):
    opcao = input("informe a operação\n1- Criar Banco \n2- Manipular Bancos \n2- Criar Cliente \n3- Imprimir Clientes \n")

    if opcao == '1':
        nome = input("Informe o nome do banco\n")
        banco01 = Banco(nome)
        listaDeBanco.append(banco01)

    elif opcao == '2':
        opcao = input("Informe o nome do Banco\n")
        banco = localizarBanco(nome)


        if (banco is not None):
            print("Bem Vindo ao Banco", banco.nome)
            flagBanco = True

            while(flagBanco):
                opcao = input("Informe uma Operação \n1 - Depositar \n2- Criar Clientes \n3- Listar clientes")

                if opcao == '1':
                    nomeCliente = input("Informe o nome do cliente\n")
                    valorDeposito = float(input("Informe o valor do deposito\n"))
                    banco.depósito(nomeCliente, valorDeposito)

                elif opcao == '2':
                    nomeCliente = input("Informe o nome do Cliente\n")
                    senha = input("Informe a senha\n")
                    banco.criarCliente(nomeCliente, senha)

                elif opcao == '3':
                    banco.imprimirListaCliente()

                elif opcao == '0':
                    flagBanco = False
    elif opcao == '0':
        flagBacen = False





# banco01.criarCliente('guilherme', '1234')
# banco01.criarCliente('joao', '1234')



# banco02 = Banco('brasilcod')
# banco02.criarCliente('pedro', '1234')
# banco02.criarCliente('mateus', '1234')

# banco02.addMalPagador('rafael')



# banco01.imprimirListaCliente()
# banco02.imprimirListaCliente()