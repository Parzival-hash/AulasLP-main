# variavelLista = [ ]

# n = int(input("Digite a quantidade de numeros sua lista: "))

# for x in range(n):
#     variavelLista += input("Insira o valor: ")
#     variavelLista[x] = int(variavelLista[x])


# for n in range(1, -1):
#     print("valores:", variavelLista[n])

# # print("Os numeros digitados foram:", variavelLista[] )



variavelVetor = []

valorInicial = int( input("Entre com o valor Inicial: "))
valorFinal = int( input("Entre com o valor Final: "))

for n in range(valorInicial, valorFinal):
    variavelVetor.append(int( input("Entre com um valor: ")))


for n in range(valorFinal-valorInicial-1,-1,-1):
    print("Valor é:", variavelVetor[n])