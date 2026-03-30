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
    option =""
    while option !="exit":
        option = input("Write the option:\n 1.Add\n 2.Search\n 3.Remove\n 4.Exit\n")
        option = option.lower().strip()
        if option == "add":
            add(c)
        elif option == "search":
            search()
        elif option == "remove":
            remove()
        elif option == "exit":
            print("Exit menu")
        else:
            print("INVALID OPTION!!!\n")
    

def add(contador):
        df = False
        while not df:
            try:
                id = int(input("Write the ID: "))
                nombre = input("Write the name: ")
                apellido = input("Write the last name: ")
                edad = int(input("Write the age: "))
                nivel = input("Write the level of english: ")
                contador+=1
                coders[contador]= {"id":id,"nombre":nombre,"apellido":apellido,"edad":edad,"nvlIngles":nivel}
                print(coders)
                df = True
            except:
                print("INVALID INPUT!!!\n")
                
        return contador

def search():
    df = False
    while not df:
        try:
            busqueda_id = int(input("Write the ID to search: "))
            coder_encontrado = "The ID does not exit\n"
            for llave, datos in coders.items():
                if datos["id"] == busqueda_id:
                    coder_encontrado = datos
            print(coder_encontrado)
            df = True
        except:
                print("INVALID INPUT!!!\n")

def remove():
    df = False
    while not df:
        try:
            rem = int(input("Write the number of the regitry to remove:"))
            del (coders[rem])
            df = True
        except:
                print("INVALID INPUT!!!\n")


menu()
