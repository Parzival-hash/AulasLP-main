def bemVindo(nomeUsuario, saldo):
    print("\n#################################\n")
    print("Seja Bem-Vindo(A)", nomeUsuario)
    print("Seu saldo atual é de R$",saldo)
    print("\n#################################\n")
    print("1- Saque \n2- Deposito \n3- Pix \n4- Extrato \n5- Criar Conta \n9- Sair do Banco")
    print("\n#################################\n")

def saque(valor,saldo):
    if(valor<=saldo):
        saldo = saldo - valor

        extrato.append(valor)
        operacao.append("-")
    else:
        print("Saldo insuficiente para realizar a operação!")
    return saldo


def deposito(valor,cliente):
    saldo = saldo + valor

    extrato.append(valor)
    operacao.append("+")
    return saldo



def pix(valor, saldo):
    if(valor<=saldo):
        saldo =saldo - valor

        extrato.append(valor)
        operacao.append("-")
    else:
        print("Saldo insuficiente para realizar a operação!")
    return saldo

#0 = Nome - string
#1 = lista de extrato - vetor
#2 = lista de operacao - vetor
#3 = saldo - Float
listaContas = [['mateus', [],[], 0.0],['joao', [],[], 0.0]]


flag = False 

while(True):

    flagCliente = True

    nome_User = input("Informe seu nome: ")

    index = -1
    for x in range(0, len(listaContas)):
        if listaContas[x][0] == nome_User:
            index = x

    if(index > -1):
        index = int(input("informe o usuario: "))
        cliente = listaContas[index]
        nomeUsuario = cliente[0]
        extrato = cliente[1]
        operacao = cliente[2]
        saldo = cliente[3]

        while(flagCliente):
                
            bemVindo(nomeUsuario, saldo)
            opcao = int(input("informe a opção: "))
            if(opcao == 1):
                valorSaque = int(input("Qual é o valor para Saque?"))
                saldo = saque(valorSaque,saldo)
                print("Seu saldo atual é de R$",saldo)
            elif(opcao == 2):
                valorDeposito = int(input("Qual é o valor para Deposito?"))
                saldo = deposito(valorDeposito,saldo)
                print("Seu saldo atual é de R$",saldo)
            elif(opcao == 3):
            
                pixTransf = int(input("Chave pix: "))
                valorPix = int(input("Qual é o valor da transferencia?"))
                saldo = pix(valorPix,saldo)
                print("Seu saldo atual é de R$",saldo)   
            elif(opcao == 4):
                for x in range(0,len(operacao)):
                    print(operacao[x], extrato[x])
            
            
            elif(opcao == 9):
                flag = False
                cliente[1] = extrato
                cliente[2] = operacao
                cliente[3] = saldo
                print(nomeUsuario, "Você foi deslogado")


        else:
            print("User", nome_User, "Não encontrado")