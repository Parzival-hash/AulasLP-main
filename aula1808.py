variavelLista = [ ]

n = int(input("Digite a quantidade de numeros sua lista: "))

for x in range(n):
    variavelLista += input("Insira o valor: ")
    variavelLista[x] = int(variavelLista[x])


print("Os numeros digitados foram:", variavelLista )