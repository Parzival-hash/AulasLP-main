# elif:

# a = 3

# if (a == 0):
#     print("Sim")
# elif(a == 1):
#     print("Não")
# else:
#     print("nada")

# ==================================

# vetores:

# lista = [ 'batata', 'pera', 'maça', 'uva']
# lista_valores = [10.30, 9.50, 7.30, 5]

# print(lista[1])

# for x in range(0,len(lista)):
#     print("Produto:", lista[x],"Valor:", lista_valores[x])


# =============================================

# exercicio

Flag = True

listaProdutos = ['maça', 'banana', 'pera', 'uva', 'morango']
listaValores = [10.30, 9.50, 7.30, 5, 7.20]

valoresMaca = 0
valoresBanana = 0
ValoresPera = 0
valoresUva = 0
valoresMorango = 0

while Flag:
    print("Bem vindo ao mercado GM, Para continuar escolha seu caminho\n")
    escolha1 = input("1-Menu\n2-Exit\n")

    if escolha1 == "2":
        Flag = False

    if escolha1== "1":
            escolha2 = input("\n1-Lista de Produtos\n2-realizar compra\n3-voltar\n")
            
            print("Insira a quantidade dos produtos que deseja, Caso não desejar o produto coloque '0'\n")
            if escolha2 == "1":
                for x in range(0,len(listaProdutos)):
                    print("Produto:", listaProdutos[x], "R$", listaValores[x])
            
            if escolha2 == "2":
                somaProduto = 0
                contProdutoDif = 0

                quantMaca = int ( input("quantidades de maça:"))
                if quantMaca > 0:
                    contProdutoDif = contProdutoDif+1
                    valoresMaca = listaValores[0]*quantMaca

                quantBanana = int ( input("quantidades de banana:"))
                if quantBanana > 0:
                    contProdutoDif = contProdutoDif+1
                    valoresBanana = listaValores[1]*quantBanana

                quantPera = int ( input("quantidades de pera:"))
                if quantPera > 0:
                    contProdutoDif = contProdutoDif+1
                    ValoresPera = listaValores[2]*quantPera

                quantUva = int ( input("quantidades de uva:"))
                if quantUva > 0:
                    contProdutoDif = contProdutoDif+1
                    valoresUva = listaValores[3]*quantUva

                quantMorango = int ( input("quantidades de morango:"))
                if quantMorango > 0:
                    contProdutoDif = contProdutoDif+1
                    valoresMorango = listaValores[4]*quantMorango


                valorCompraSDesconto = valoresMaca+valoresBanana+ValoresPera+valoresUva+valoresMorango


                if contProdutoDif >= 3 and contProdutoDif <=4:
                    print("\ndesconto de %10:", valorCompraSDesconto*0.1)
                    print("\nValor com %10 desconto:", valorCompraSDesconto - valorCompraSDesconto*0.1)
                
                elif( contProdutoDif >=5):
                    print("\nDesconto de %20:", valorCompraSDesconto*0.2)
                    print("\nValor do Valor Total:", valorCompraSDesconto - valorCompraSDesconto*0.2)
                else:
                    print("Sem Desconto")
                    print("Valor Total:", valorCompraSDesconto)