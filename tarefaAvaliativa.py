# 0 = nome - String
# 1 = extrato - Lista
# 2 = operacoes - Lista
# 3 = saldo - float
# 4 = senha - String
listaContas = [['guilherme',[],[],0.0,'12345'],['joao',[],[],0.0,'12345']]
listaFuncionarios = [['joao','12345'],['pedro','12345']]

senha='12345'

def menu(nomeUsuario,saldo):
    print("\n#################################\n")
    print("Seja Bem-Vindo(A)", nomeUsuario)
    print("Seu saldo atual é de R$",saldo)
    print("\n#################################\n")
    print("1- Saque \n2- Deposito \n3- Pix \n4- Extrato \n5- Criar Conta \n9- Sair do Banco")
    print("\n#################################\n")
    
def deposito(valor,saldo):
    saldo =saldo+valor
    extrato.append(valor)
    operacoes.append('+')
    return saldo


def saque (valor,saldo):
    if(valor<=saldo):
        saldo = saldo - valor
    else:
        print("Você não tem Saldo!")
    return saldo


def buscar_em_vetores(valorBusca,listaBusca):
    index = -1
    for x in range(0,len(listaContas)):
        if listaBusca[x][0] == valorBusca:
                index = x
    return index

def buscarFuncionario(valorBusca,listaBusca):
    index = -1
    for x in range(0,len(listaFuncionarios)):
        if listaBusca[x][0] == valorBusca:
                index = x
    return index

def transferencia(saldo):
    informeClientes = input("informe o nome do cliente: ")
    index = buscar_em_vetores(informeClientes,listaContas)
    if(index>-1):
        print("Informe o valor para transferir para o(a): ",listaContas[index][0] )
        informeValor = float(input("informe um valor: "))
        if(informeValor<=saldo):
            saldo = saldo - informeValor
            listaContas[index][3]+=informeValor
        else:
            print('Sem saldo!')
    return saldo
        


def listarPessoa(tipo):
    if(tipo==1):
        for cliente in listaContas:
            print("Cliente: ",cliente[0],"Senha: ",cliente[4],'Saldo: ',cliente[3])
    elif(tipo==2):
        for funcionario in listaFuncionarios:
            print("funcionario: ",funcionario[0],"Senha: ",funcionario[1])


def adicionarPessoa(tipo):
    novoUsuario=input('Informe o nome de usuario/funcionario:')
    novaSenha=input('Informe a senha de usuario:')

    if(tipo==1):
        listaContas.append([novoUsuario,[],[],0.0,novaSenha])

    elif(tipo==2):
        listaFuncionarios.append([novoUsuario,novaSenha])

    print("Funcionario Adicionado!")

    









while(True):

    funcionario = int(input('Você é um funcionario? 1-sim; 2-não: '))

    if (funcionario==1):


        nomeFuncionario = input("informe seu Login: ")
        index = buscarFuncionario(nomeFuncionario,listaFuncionarios)
        
        if(index>-1):    
            funcionarioConta = listaFuncionarios[index]
            senhaInformada = input('Então informe sua senha master: ')

            if(funcionarioConta[1]==senhaInformada):
                opcaoFuncionario= int(input("Deseja acessar opções usuario ou funcionario?? 1-Usuario 2-Funcionario\n"))

                if(opcaoFuncionario==1):
                    print('Digite 1 - para criar usuario')
                    print('Digite 2 - listar usuarios')

                    operacaoFuncionario = int(input('informe a operação: '))

                    if(operacaoFuncionario==1):
                        adicionarPessoa(opcaoFuncionario)

                    elif(operacaoFuncionario==2):
                        listarPessoa(operacaoFuncionario)

                    else:
                        print("Opção Invalida......")



                elif(opcaoFuncionario==2):
                    print('Digite 1 - para criar Funcionario')
                    print('Digite 2 - listar Funcionario')

                    operacaoFuncionario = int(input('informe a opção: '))

                    if(operacaoFuncionario==1):
                     adicionarPessoa(opcaoFuncionario)

                    elif(operacaoFuncionario==2):
                        listarPessoa(operacaoFuncionario)

                    else:
                        print("Opção Invalida......")



    elif (funcionario==2):

        flagCliente = True
        nome_user = input("Informe nome usuario cliente: ")
        index = buscar_em_vetores(nome_user,listaContas)


        if(index>-1):    
            cliente = listaContas[index]
            senhaInformada = input('Então informe sua senha master: ')


            if(cliente[4]==senhaInformada):
                nomeUsuario=cliente[0]
                extrato = cliente[1]
                operacoes = cliente[2]
                saldo = cliente[3]


                while(flagCliente):
                    menu(nomeUsuario,saldo)
                    opcao = int(input("Informe a opcão: "))


                    if(opcao==1):
                        valor_de_saque = int(input("Qual é o valor para saque ?:"))
                        saldo = saque(valor_de_saque,saldo)
                        print("Seu saldo Atual:", saldo)


                    elif(opcao==2):
                        valor_de_deposito = int(input("Qual é o valor para depósito ?:"))
                        saldo = deposito(valor_de_deposito,saldo)
                        print("Seu saldo Atual:", saldo)


                    elif(opcao==3):
                        print("Seu Extrato!")
                        for x in  range(0,len(operacoes)):
                            print(extrato[x],operacoes[x])


                    elif(opcao==4):
                         print("Opacao de transferencia")
                         saldo = transferencia(saldo)


                    elif(opcao==0):
                        flagCliente = False
                        cliente[1] = extrato
                        cliente[2] = operacoes 
                        cliente[3] = saldo
                        print(nomeUsuario," vc foi deslogado.........")


            else:
                print("User: ",nome_user, " senha incorreta")   


        else:
            print("User: ",nome_user, " não foi localizado...")

## Oque falta ?
    # 1 - Criar extrato
    # 2 - Criar Sistema de Usuário
    # 3 - Criar Sistema de Transferência 
