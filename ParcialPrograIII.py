def ClienteCodigo():
    while True:
        codigocliente = input("Ingrese el codigo del cliente: ")
        if codigocliente == "":
            print("No puede dejar vacio este campo")
        else:
            return codigocliente


def ClienteNombre():
    while True:
        nombreCliente = input("Ingrese el nombre del Cliente: ")
        if nombreCliente == "":
            print("No puede dejar vacio este campo")
        else:
            return nombreCliente


def DireccionCliente():
    while True:
        direccionCliente = input("Ingrese la direccion del cliente ")
        if direccionCliente == "":
            print("No puede dejar vacio este campo")
        else:
            return direccionCliente


def TelefonoCliente():
    while True:
        telefonoCliente = input("Ingrese el numero de telefono del cliente ")
        if telefonoCliente == "":
            print("No puede dejar vacio este campo")
        else:
            return telefonoCliente


def ImprimirClientes():
    if len(clientes) == 0:
        print("No existe ningun cliente en nuestro registro")
    else:
        clientes.sort()
        print("\n".join(i[0] + " - " + str(i[1])+ " - " +str(i[2]) + " - " + str(i[3])  for i in clientes))


def CodigoDeProyecto():
    while True:
        codigoProyecto = input("Codigo del Proyecto: ")
        if codigoProyecto == "":
            print("No puede dejar vacio.")
        else:
            return codigoProyecto


def DescripcionDeProyecto():
    while True:
        nombreProyecto = input("Nombre del Proyecto: ")
        if nombreProyecto == "":
            print("Debe ingresar un nombre de Proyecto ")
        else:
            return nombreProyecto


def EstadoDeProyecto():
    while True:
        estadoProyecto = input("Estado del Proyecto: ")
        if estadoProyecto == "":
            print("Debe ingresar un estado del proyecto.")
        else:
            return estadoProyecto


def IdCliente():
    while True:
        codigoCliente = input("Codigo del Cliente: ")
        if codigoCliente == "":
            print("No puede dejar vacio.")
        else:
            return codigoCliente


def MostrarProyectos():
    if len(proyectos) == 0:
        print("La lista esta Vacia.")
    else:
        proyectos.sort()
        print("\n".join(i[0] + " - " + str(i[1])+ " - " +str(i[2]) + " - " +str(i[3]) for i in proyectos))


def CodigoRegion():
    while True:
        codigoRegion = input("Codigo de Region: ")
        if codigoRegion == "":
            print("No puede dejar vacio.")
        else:
            return codigoRegion


def IngresarMunicipio():
    while True:
        nombreMunicipio = input("Nombre del Municipio: ")
        if nombreMunicipio == "":
            print("Debe ingresar un nombre de Municipio ")
        else:
            return nombreMunicipio


def IngresarDepartamento():
    while True:
        codigoDepartamento = input("Nombre del Departamento: ")
        if codigoDepartamento == "":
            print("Debe ingresar un Nombre de Departamento.")
        else:
            return codigoDepartamento


def ImprimirRegion():
    if len(CodigoDeRegion) == 0:
        print("La lista esta Vacia.")
    else:
        CodigoDeRegion.sort()
        print("\n".join(i[0] + " - " + str(i[1])+ " - " +str(i[2]) for i in CodigoDeRegion))


def RegistroProyecto():
    if len(proyectos) == 0:
        print("La lista esta Vacia.")
    else:
        proyectos.sort()
        print("\n".join(i[0] + " - " + str(i[1])+ " - " +str(i[2])for i in proyectos)
        + " - "+"\n".join(i[0] + " - " + str(i[1])+ " - " +str(i[2])for i in clientes))


def borrarCliente():
    if len(clientes) == 0:
        print("No se ha ingresado ningun cliente.")
    else:
        codigo = ClienteCodigo()
        indice = buscarCliente(codigo)
        if indice == -1:
            print("No se ha encontrado el cliente '{}'".format(codigo))
            return False
        print("Se ha eliminado el cliente '{}' con nombre {}".format(codigo, clientes[indice][1]))
        del clientes[indice]
        return True



def buscarCliente(nombre):
    for i, e in enumerate(clientes):
        if e[0] == nombre:
            return i
    return -1



def borrarProyecto():

    if len(proyectos) == 0:
        print("No se ha ingresado ningun Proyecto ")
    else:
        codigo = CodigoDeProyecto()
        indice = buscarProyecto(codigo)
        if indice == -1:
            print("No se ha encontrado el Proyecto '{}'".format(codigo))
            return False

        print("Se ha eliminado el proyecto '{}' con nombre {}".format(codigo, proyectos[indice][1]))
        del proyectos[indice]
        return True


def buscarProyecto(nombre):
    for i, e in enumerate(proyectos):
        if e[0] == nombre:
            return i
    return -1


def borrarRegion():

    if len(CodigoDeRegion) == 0:
        print("No se ha ingresado ninguna Region ")
    else:
        codigo = CodigoRegion()
        indice = buscarRegion(codigo)
        if indice == -1:
            print("No se ha encontrado Ninguna Region '{}'".format(codigo))
            return False

        print("Se ha eliminado La Region '{}' con nombre {}".format(codigo, CodigoDeRegion[indice][1]))
        del CodigoDeRegion[indice]
        return True


def buscarRegion(nombre):
    for i, e in enumerate(CodigoDeRegion):
        if e[0] == nombre:
            return i
    return -1


def Menu():
    print("************************************************************************")
    print("Ingrese la opcion a elegir...")
    print("-------- MENU  DE OPCIONES --------------")
    print("\t1 - Registrar a un Cliente.")
    print("\t2 - Listado de clientes.")
    print("\t3 - Ingreso de Proyectos.")
    print("\t4 - Mostrar Proyectos.")
    print("\t5 - Ingresar Municipio y Departamento ")
    print("\t6 - Listado de Municipios y Departamentos ")
    print("\t7 - Registro de Proyectos ")
    print("--------- OTRAS OPCIONES --------------- ")
    print("\t8 - Eliminar ")
    print("\t0 - Salir")
def menu2():

    print("Seleccione una opción...")
    print("***Opcion para eliminacion de Datos***")
    print("a - Eliminar a un Cliente ")
    print("b - Eliminar a un  Proyecto ")
    print("c - Eliminar una Region ")
    print("d - Regresar al Menu principal ")

clientes = []
proyectos = []
CodigoDeRegion = []


while True:
    Menu()

    try:
        opcion = int(input("Ingrese el número de la opción escogida: "))
    except:
        opcion = -1

    if opcion == 1:
        clientes.append((ClienteCodigo(),ClienteNombre(), DireccionCliente(),TelefonoCliente()))
    elif opcion == 2:
        ImprimirClientes()
    elif opcion == 3:
        proyectos.append((CodigoDeProyecto(),DescripcionDeProyecto(),EstadoDeProyecto(),IdCliente()))
    elif opcion == 4:
        MostrarProyectos()
    elif opcion == 5:
        CodigoDeRegion.append((CodigoRegion(),IngresarMunicipio(),IngresarDepartamento()))
    elif opcion == 6:
        ImprimirRegion()
    elif opcion == 7:
         RegistroProyecto()
    elif opcion == 8:
        menu2()

        opcion2 = input(" Ingrese la Letra que desea elegir ")

        if opcion2 == "a":
            borrarCliente()
        if opcion2 == "b":
            borrarProyecto()
        if opcion2 == "c":
            borrarRegion()
        if opcion2 == "d":
            break

    elif opcion == 0:
        break
    else:
        print("La opción ingresada no es correcta, indica una opción correcta")