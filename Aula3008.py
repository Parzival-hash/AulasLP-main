
def menu(nomeUsuario, saldo):
    print("\n#################################\n")
    print("Seja Bem-Vindo(A)", nomeUsuario)
    print("Seu saldo atual é de R$",saldo)
    print("\n#################################\n")
    print("1- Saque \n2- Deposito \n3- Pix \n0- Sair do Banco")
    print("\n#################################\n")

def saque(valor,saldo):
    if(valor<=saldo):
        saldo =saldo-valor
    else:
        print("Saldo insuficiente para realizar a operação!")
    return saldo

def deposito(valor,saldo):
    if(valor<=saldo):
        saldo =saldo-valor
    else:
        print("Saldo insuficiente para realizar a operação!")
    return saldo


def pix(valor, saldo):
    if(valor<=saldo):
        saldo =saldo-valor
    else:
        print("Saldo insuficiente para realizar a operação!")
    return saldo

flag = True
nomeUsuario = input("Insira seu Nome: ")
saldo = 10
extrato = []


while(flag):
    menu(nomeUsuario, saldo)
    opcao = int(input("informe a opção: "))

    if(opcao == 1):
        valorSaque = int(input("Qual é o valor para Saque?"))
        print("Seu saldo atual é de R$",saldo)

    elif(opcao == 2):
        valorDeposito = int(input("Qual é o valor para Deposito?"))
        saldo = deposito(valorDeposito,saldo)
        print("Seu saldo atual é de R$",saldo)

    elif(opcao == 3):
        pixTransf = int(input("Chave pix: "))
        valorPix = int(input("Qual é o valor da transferencia?"))
        saldo = deposito(valorPix,saldo)
        print("Seu saldo atual é de R$",saldo)        

    elif(opcao == 4):
        for x in range():
            extrato[x] = int(extrato[x])
            extrato[x] = extrato[x] + extrato [x]
        
        print(extrato)
        

    elif(opcao == 0):
        flag = False
        print(nomeUsuario, "Você foi deslogado")
