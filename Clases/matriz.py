num = int(input("Ingrese un numero: "))
if num <= 0 :
    print("Numero invalido")
elif num == 1:
    print(1)
else:
    matriz = []
    for i in range (0, num, 1):
        matriz. append([1]*num)
    
    for i in range (1, num, 1):
        for j in range (1, num, 1):
            valor_ant = matriz[i][j-1]
            valor_arr = matriz[i-1][j]
            matriz[i][j] = valor_ant + valor_arr
            valor = matriz[i][j]
    
    for i in range (0, num, 1):
        print("")
        for j in range (0, num, 1):
            print(matriz[i][j],end="")