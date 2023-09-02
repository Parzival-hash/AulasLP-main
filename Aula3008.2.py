def bemVindo(nomeUsuario, saldo):
    print("\n#################################\n")
    print("Seja Bem-Vindo(A)", nomeUsuario)
    print("Seu saldo atual é de R$",saldo)
    print("\n#################################\n")
    print("1- Saque \n2- Deposito \n3- Pix \n4- Extrato \n5- Criar Conta \n0- Sair do Banco")
    print("\n#################################\n")

def saque(valor,saldo):
    if(valor<=saldo):
        saldo = saldo - valor

        extrato.append(valor)
        operacao.append("-")
    else:
        print("Saldo insuficiente para realizar a operação!")
    return saldo


def deposito(valor,saldo):
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

novoUsuario = []

bancoDeDados = [ [1, 1], [2, 2], [3, 3]]












flag = True
nomeUsuario = input("Insira seu Nome: ")
saldo = 10
extrato = []
operacao = []

while(flag):
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
    
    elif(opcao == 5):
        novoUsuario.append(['rafael',0])
        novoUsuario[-1][0].append(input("Digite seu nome:"))
        codigo = input("Codigo desejado em um digito:")
        novoUsuario[0].append(codigo)

        if (codigo != bancoDeDados):
            print("Nome de Usuario:", novoUsuario[0][0], "\nNumero do banco", novoUsuario[0][1])
        else :
            print("Digito já existente")
        

        

    elif(opcao == 0):
        flag = False
        print(nomeUsuario, "Você foi deslogado")