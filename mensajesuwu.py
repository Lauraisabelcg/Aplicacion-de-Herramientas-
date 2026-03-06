from GestionarJson import cargar, crear, generar_id
from Validaciones import nombrevalido
from FuncionesS import existenombreS
from datetime import date

ARCHIVO_USUARIOS="Usuarios.json"
archivo_mensajes="mensaje.json"


def mensajes():
    mensajes=cargar(archivo_mensajes)
  

    nombre=input("Escriba el nombre del usuario: ")
    while nombrevalido(nombre)==False:
        print("Este nombre esta vacio, escriba el nombre del usuario: ")
        nombre=input("Escriba el nombre del usuario: ")
    if existenombreS(nombre)==True:
           
           
        Lista_mensajes={
        "id":generar_id(mensajes),
        "fecha":str(date.today()),
        "Detalle":input("¿Que desea comunicar al Administrador?")
            
        }
    mensajes.append(Lista_mensajes)
    crear(archivo_mensajes,mensajes)
    print("Mensaje enviado correctamente")

def lista_mensajes():
    mensajes=cargar(archivo_mensajes)
    for elemento in mensajes:
        print(f"ID:{elemento['id']}")
        print(f"fecha:{elemento['fecha']}")
        print(f"Detalle:{elemento['Detalle']}")
        print("-"*20)

