# var1 = input("Quantos anos você tem?")

# ===================================================
# flag = True

# while flag:
#     var2 = input("Coloque um numero para o var2")
#     print(type(var2))

#     if var2 == "exit":
#         flag=False

# ===================================================

contador = 0
flag = True

while flag:
    
    var_x = int (input("informe o valor de X"))
    var_y = int (input("informe o valor de Y"))

    varTipo = input("informe o tipo da operação: adição, divisão, subtração, multiplicação. Ou digite 'Exit'")


    if varTipo == "Exit":
        flag = False


    if varTipo =="adição":
        print(var_x + var_y)

    if varTipo =="divisão":
        while(var_x >= 0):
            var_x = var_x - var_y
            contador = contador + 1
        print("resultado:", contador)

    if varTipo =="subtração":
        print(var_x - var_y)

    if varTipo =="multiplicação":
        for x in range(0,var_y-1):
            var_x = var_x + var_y
        print("resultado:", var_x)