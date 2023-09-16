# 0 = nome - String
# 1 = extrato - Lista
# 2 = operacoes - Lista
# 3 = saldo - float
# 4 = senha - String
listaContas = [['rafael',[],[],0.0,'12345'],['angelo',[],[],0.0,'12345']]

senha='12345'

def menu(nomeUsuario,val):
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
        print("Você não tem Saldo, volte à trabalhar !!!")
    return saldo

def buscar_em_vetores(valorBusca,listaBusca):
    index = -1
    for x in range(0,len(listaContas)):
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
            print('Sem dinheiro!!!!')
    return saldo
        
        
    

def adicionar_novo_usuario():
    novoUsuario=input('Informe o nome de usuario:')
    novaSenha=input('Informe a senha de usuario:')
    listaContas.append([novoUsuario,[],[],0.0,novaSenha])
    print("Usuario Adicionado!")
    
def listar_clientes():
    for cliente in listaContas:
        print("Cliente: ",cliente[0],"Senha: ",cliente[4],'Saldo: ',cliente[3])
        

while(True):
    funcionario = int(input('Você é um funcionario? 1-sim; 2-não: '))
    if (funcionario==1):
        senhaInformada = input('Então informe sua senha master: ')
        if(senha==senhaInformada):
            print('Digite 1 - para criar usuario')
            print('Digite 2 - listar usuarios')
            operacaoFuncionario = int(input('informe a operação: '))
            if(operacaoFuncionario==1):
                adicionar_novo_usuario()
            elif(operacaoFuncionario==2):
                listar_clientes()
            else:
                print("Opção Invalida......")
        else:
            print("Senha Invalida")
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
