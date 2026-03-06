from GestionarJson import cargar, crear, generar_id
from Validaciones import nombrevalido, ValidarEntero, Validarn_Telefono, ValidarEnteroyNega

ARCHIVO_USUARIOS="Usuarios.json"

def existenombre(nombre,apellido):
    usuarios=cargar(ARCHIVO_USUARIOS)
    for elemento in usuarios:
        if nombre.lower()==elemento["nombre"].lower() and apellido.lower()==elemento["apellido"].lower():
            return True
    return False

def agregar_usuarios():
    usuarioss=cargar(ARCHIVO_USUARIOS)
    nombre=str(input("Escriba el nombre del usuario que quiere crear: "))
    apellido=str(input("Escriba el apellido del usuario: "))
    while nombrevalido(nombre)==False:
        print("Este nombre esta vacio, escriba el nombre del usuario: ")
        nombre=str(input("Escriba el nombre del usuario: "))
        apellido=str(input("Escriba el apellido del usuario: "))
    while existenombre(nombre,apellido)==True:
        print("Este nombre y apellido ya existe, escriba un nombre y apellido que no este registrado: ")
        nombre=str(input("Escriba el nombre del usuario: "))
        apellido=str(input("Escriba el apellido del usuario: "))
        ##debo comprobar si este if sirve o si vuelvo a repetir, entonces ahi se registra
    while existenombre(nombre,apellido)==False:
        telefono_U=Validarn_Telefono("Escriba su numero de telefono: ",1000000000,9999999999)
        while telefono_U==None:
            telefono_U=Validarn_Telefono("Intente de nuevo,escriba su numero de telefono: ",1000000000,9999999999)
        direccion=ValidarEnteroyNega("Escriba el numero de su torre: ",1)
        while direccion==None:
            print(" intente nuevamente: ")
            direccion=ValidarEnteroyNega("Escriba el numero de su torre: ",1)
        direccion_Ap=ValidarEnteroyNega("Escriba el numero de su apartamento: ",1)
        while direccion_Ap==None:
            print(" intente nuevamente: ")
            direccion_Ap=ValidarEnteroyNega("Escriba el numero de su torre: ",1)
        Lista_usuarioss={
            "id":generar_id(usuarioss),
            "nombre":nombre,
            "apellido":apellido,
            "telefono":telefono_U,
            "direccion torre": direccion,
            "apartamento":direccion_Ap
        }
        usuarioss.append(Lista_usuarioss)
        crear(ARCHIVO_USUARIOS,usuarioss)
    print("Usuario creado con exito")

def lista_usuarioss():
    usuarioss=cargar(ARCHIVO_USUARIOS)
    for elemento in usuarioss:
        print(f"ID:{elemento['id']}")
        print(f"nombre:{elemento['nombre']}")
        print(f"apellido:{elemento['apellido']}")
        print(f"telefono:{elemento['telefono']}")
        print(f"direccion torre:{elemento['direccion torre']}")
        print(f"apartamento:{elemento['apartamento']}")
        print("-"*20)

def actualizar_U():
    actualizar=cargar(ARCHIVO_USUARIOS)
    lista_usuarioss()
    new_id_all=ValidarEntero("Escriba el numero del ID del usuario al que desea cambiarle la informacion ")

    for elemento in actualizar:
        if new_id_all==elemento['id']:
            new_id_all=input("Ingrese el nuevo nombre del usuario ")
            elemento['nombre']=new_id_all
            new_id_all=input("Ingrese el nuevo apellido del usuario ")
            elemento['apellido']=new_id_all
            new_id_all=Validarn_Telefono("Ingrese el nuevo numero de telefono del usuario ",1000000000,9999999999)
            elemento['telefono']=new_id_all
            new_id_all=ValidarEnteroyNega("Ingrese el numero de la torre del usuario ",1)
            elemento['direccion torre']=new_id_all
            new_id_all=ValidarEnteroyNega("Ingrese el numero del apartamento del usuario ",1)
            elemento['apartamento']=new_id_all

            crear(ARCHIVO_USUARIOS,actualizar)
            print("Usuario actualizado")
            return
    print("El usuario no existe. \n")

def eliminar_usuarios():
    contadorU=0
    eliminar=cargar(ARCHIVO_USUARIOS)
    lista_usuarioss()
    eliminar_U=ValidarEntero("Escoja el id del usuario a eliminar")
    while eliminar_U==None:
        eliminar_U=ValidarEntero("Error,escoja el id del usuario a eliminar")
    for elemento in eliminar:
        if eliminar_U==elemento["id"]:
            eliminar.pop(contadorU)
            crear(ARCHIVO_USUARIOS,eliminar)
            print("usuario eliminado con exito")
            return
        contadorU+=1
    print("El usuario no existe. \n")


