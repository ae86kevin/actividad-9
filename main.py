Dviajes = {}


def contadordestinos(viajes):
    if viajes =="":
        return 0
    else:
        return viajes.count("destino")


seleccion = ""
while seleccion != "0":
    print("\nmenu principal")
    print("1. Cuántos clientes desea ingresar?")
    print("2. Listado de clientes y destinos visitados")
    print("0. Salir...")
    seleccion = input()

    if seleccion == "1":
        cantidad = int(input("\nIngrese la cantidad de clientes: "))

        for i in range(cantidad):
            print(f"\nIngrese los datos del cliente {i + 1}")
            codigo = input("Ingrese el código del cliente: ")
            Dviajes[codigo] = {}
            Dviajes[codigo]["nombre"] = input("Ingrese el nombre del cliente: ")
            Dviajes[codigo]["viajes"] = {}

            cantidadDestinos = int(input("\nIngrese la cantidad de destinos: "))
            for j in range(cantidadDestinos):
                destino = input(f"Ingrese el nombre del destino {j + 1}: ")

                Dviajes[codigo]["viajes"][destino] = {"nombre del destino": destino}

    elif seleccion == "2":
        print("\nListado de clientes y destinos visitados:")

        for codigo, datos in Dviajes.items():
            print(f"\nCodigo: {codigo}")
            print(f"Nombre: {datos['nombre']}")
            print("Destinos")
            for destino, a in datos["viajes"].items():
                print(f"Nombre del destino: {a['nombre del destino']}")


        print(f"cantidad de viajes visitados: {contadordestinos(datos)}"







