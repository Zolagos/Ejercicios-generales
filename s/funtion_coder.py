c = 3
coders = {
    1: {
        "id": 1048229292,
        "nombre": "Jander",
        "apellido": "Arguello",
        "edad": 30,
        "nvlIngles": "-A0"
    },
    2: {
        "id": 1048229296,
        "nombre": "Luisa",
        "apellido": "De la Rosa",
        "edad": 19,
        "nvlIngles": "C30"
    },
    3: {
        "id": 1048229297,
        "nombre": "Maria",
        "apellido": "Sanchez",
        "edad": 19,
        "nvlIngles": "C1"
    }
}
def menu ():
    option = input("Write the option:\n 1.Add\n 2.Search\n 3.Remove\n 4.Exit\n")
    option = option.lower().strip()
    if option == "add":
        id = int(input("Digite el ID: "))
        nombre = input("Digite el nombre: ")
        apellido = input("DIgite el apellido: ")
        edad = int(input("Digite la edad: "))
        nivel = input("Digite el nivel de ingles: ")
        coders[c]= {"id":id,"nombre":nombre,"apellido":apellido,"edad":edad,"nvlIngles":nivel}
        print(coders)
    elif option == "search":
        busqueda_id = int(input("Digite el ID que desea buscar: "))
        coder_encontrado = "No existe"
        for llave, datos in coders.items():
            if datos["id"] == busqueda_id:
                coder_encontrado = datos
        print(coder_encontrado)
    elif option == "remove":
        rem = int(input("wich ID desea eleminar:\n"))
        del (coders[rem])
