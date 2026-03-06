from GestionarJson import cargar, crear, generar_id
from Validaciones import Validarn_herramientas, nombrevalido, ValidarEntero

ARCHIVO_HERRAMIENTAS="Herramientas.json"
def existenombre(nombre):
    herramienta=cargar(ARCHIVO_HERRAMIENTAS)
    for elemento in herramienta:
        if nombre.lower()==elemento["nombre"].lower():
            return True
    return False

def agregarHerramientaActual(nombre):
    herramienta=cargar(ARCHIVO_HERRAMIENTAS)
    for elemento in herramienta:
        if nombre.lower()==elemento["nombre"].lower():
            cantidad=int(input(f'Para actualizar, ingrese las cantidades a agregar, actualmente cuenta con {elemento.get("cantidad","no existe")} '))
            elemento["cantidad"]=elemento["cantidad"]+cantidad
            print("actualizacion exitosa!")
            crear(ARCHIVO_HERRAMIENTAS,herramienta)
            return
    print('no se ejecuto la accion')

def RestarHerramienta(nombre):
    #se usa cuando alguien la solicita
    herramienta=cargar(ARCHIVO_HERRAMIENTAS)
    
    for elemento in herramienta:
        if nombre.lower()==elemento["nombre"].lower():
            cantidad=int(input(f'Para solicitar una herramienta, ingrese la cantidad que necesita, actualmente cuenta con {elemento.get("cantidad","no existe")} '))
            if cantidad>elemento["cantidad"]:
                print("no se puede prestar")
            #HACER CONDICIONAL DE SI LA CANTIDAD SOLICITADA ES MAYOR QUE LA CANTIDAD DISPONIBLE, ENTONCES SE RECHACE
            else:
                elemento["cantidad"]=elemento["cantidad"]-cantidad
                print("solicitud exitosa!")
                crear(ARCHIVO_HERRAMIENTAS,herramienta)
            return
    print('no se ejecuto la accion')

def agregarHerramientaActual(nombre):
    herramienta=cargar(ARCHIVO_HERRAMIENTAS)
    
    for elemento in herramienta:
        if nombre.lower()==elemento["nombre"].lower():
            cantidad=int(input(f'Para actualizar, ingrese las cantidades a agregar, actualmente cuenta con {elemento.get("cantidad","no existe")} '))
            elemento["cantidad"]=elemento["cantidad"]+cantidad
            print("actualizacion exitosa!")
            crear(ARCHIVO_HERRAMIENTAS,herramienta)
            return
    print('no se ejecuto la accion')

ARCHIVO_HERRAMIENTAS="Herramientas.json"
def agregar_herramienta():
    herramientas=cargar(ARCHIVO_HERRAMIENTAS)
    nombre=input("Escriba el nombre de la herramienta: ")
    while nombrevalido(nombre)==False:
        print("Este nombre esta vacio, escriba el nombre de la herramienta: ")
        nombre=input("Escriba el nombre de la herramienta: ")
    if existenombre(nombre)==True:
        agregarHerramientaActual(nombre)
    elif existenombre(nombre)==False:
        cantidad_herramienta=Validarn_herramientas("¿Cuantas herramientas tiene? ",1)
        while cantidad_herramienta==None:
            print("Cantidad no valida, intente nuevamente: ")
            cantidad_herramienta=Validarn_herramientas("¿Cuantas herramientas tiene?",1)
        valorprecio=Validarn_herramientas("Ingrese el precio unitario de esta herramienta si se daña: ",1000)
        while valorprecio==None:
            print("Precio minimo es de 1000 pesos")
            valorprecio=Validarn_herramientas("Ingrese el precio unitario de esta herramienta si se daña: ",1000)

        Lista_Herramientas={
            "id":generar_id(herramientas),
            "nombre":nombre,
            "cantidad":cantidad_herramienta,
            "valor estimado": valorprecio
        }
        herramientas.append(Lista_Herramientas)
        crear(ARCHIVO_HERRAMIENTAS,herramientas)
    print("Herramienta guardada con exito")

def lista_herramientas():
    herramientas=cargar(ARCHIVO_HERRAMIENTAS)
    for elemento in herramientas:
        print(f"ID:{elemento['id']}")
        print(f"nombre:{elemento['nombre']}")
        print(f"cantidad:{elemento['cantidad']}")
        print(f"Valor unitario si se daña:{elemento['valor estimado']}")
        print("-"*20)

def actualizar_H():
    actualizar=cargar(ARCHIVO_HERRAMIENTAS)
    lista_herramientas()
    new_nombreH=input("¿El nombre de cual herramienta desea actualizar? ")

    for elemento in actualizar:
        if new_nombreH.lower().strip()==elemento['nombre'].lower().strip():
            new_nombreH=input("Ingrese el nuevo nombre de la herramienta ")
            elemento['nombre']=new_nombreH
            crear(ARCHIVO_HERRAMIENTAS,actualizar)
            print("Herramienta actualizada")
            return
    print("La herramienta no existe. \n")

def eliminar_herramienta():
    contadorH=0
    eliminar=cargar(ARCHIVO_HERRAMIENTAS)
    lista_herramientas()
    eliminar_H=ValidarEntero("Escoja el id de la herramienta a eliminar")
    while eliminar_H==None:
        eliminar_H=ValidarEntero("Error,escoja el id de la herramienta a eliminar")
    for elemento in eliminar:
        if eliminar_H==elemento["id"]:
            eliminar.pop(contadorH)
            crear(ARCHIVO_HERRAMIENTAS,eliminar)
            print("Herramienta eliminada con exito")
            return
        contadorH+=1
    print("La herramienta no existe. \n")
