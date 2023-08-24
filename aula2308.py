variavelVetor = []

valorInicial = int( input("Entre com o valor Inicial: "))
valorFinal = int( input("Entre com o valor Final: "))

somaVetor = 0

# for n in range(valorInicial, valorFinal):
#     variavelVetor.append(int( input("Entre com um valor: ")))
#     somaVetor = somaVetor + variavelVetor[valorInicial]

for n in range(valorFinal-valorInicial-1,-1,-1):
    variavelVetor.append(int( input("Entre com um valor: ")))
    somaVetor = somaVetor + variavelVetor[n-valorInicial]

print("soma dos Vetores: ", somaVetor)