numero = int(input("Ingrese un numero: "))
a = 0
b = 1
for n in range (0, numero+1, 1):
    if n == 0:
        pass
    elif n == 1:
        pass
    elif n > 1:
        c = a + b
        a = b
        b = c
print (b)