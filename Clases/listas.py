colores = ["Amarillo", "Rojo", "Verde", "Azul"]
posiciones = colores.index("Azul")
existe = "Rojo" in colores
print(f"colores {colores}")
print(f"posicion {posiciones}")
print(f"existe {existe}")

colores.append("Rosado")
colores.insert(0,"negro")

def agregar_unico(color:str):
    if color in colores:
        respuesta = "no va"
    else:
        colores.append(color)
        respuesta = "siza"
    return respuesta
