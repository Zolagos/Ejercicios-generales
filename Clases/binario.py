def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

lista = [1,2,3,4,5,6,7,8,9,10]
resultado = busqueda_binaria(lista, 5)
print(f"el numero 4 se encuentra en la posicion:{resultado}")