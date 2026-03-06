from GestionarJson import cargar, generar_id, crear
from Validaciones import ValidarEntero, nombrevalido
from FuncionesS import RestarHerramienta, existeHerramienta, existenombreS
from datetime import date, datetime, timedelta 

ARCHIVO_HERRAMIENTAS="Herramientas.json"
ARCHIVO_SOLICITUDES="Solicitudes.json"
ARCHIVO_U="Usuarios.json"

def Solicitar_Herramienta():
    solicitud=cargar(ARCHIVO_SOLICITUDES)
  

    nombre=input("Escriba el nombre del usuario: ")
    while nombrevalido(nombre)==False:
        print("Este nombre esta vacio, escriba el nombre del usuario: ")
        nombre=input("Escriba el nombre del usuario: ")
    if existenombreS(nombre)==True:
        herramienta=input("Escriba el nombre de la herramienta: ")
        while nombrevalido(herramienta)==False:
            print("Este nombre esta vacio, escriba el nombre de la herramienta: ")
            herramienta=input("Escriba el nombre de la herramienta: ")

        if existeHerramienta(herramienta)==True:
            
            cantidad_actual=RestarHerramienta(herramienta)

            if cantidad_actual is None:
                print("No se pudo realizar la solicitud")
                return
            fecha_inicio=date.today()
            dias_prestamo=ValidarEntero("Ingrese cuantos dias usara la herramienta")
            fecha_devolucion=fecha_inicio+timedelta(days=dias_prestamo)

            Lista_solicitud={
            "id":generar_id(solicitud),
            "nombre":nombre,
            "herramienta":herramienta,
            "cantidad":cantidad_actual,
            "fecha inicio":str(fecha_inicio),
            "fecha de devolucion":str(fecha_devolucion)
            }
            solicitud.append(Lista_solicitud)
            crear(ARCHIVO_SOLICITUDES,solicitud)
            print("Usuario creado con exito")
        else:
            print('no se encontro la herramienta ')
    else:
        print('no se encontro el usuario')    


   

def lista_solicitud():
    solicitud=cargar(ARCHIVO_SOLICITUDES)
    for elemento in solicitud:
        print(f"ID:{elemento['id']}")
        print(f"nombre:{elemento['nombre']}")
        print(f"herramienta:{elemento['herramienta']}")
        print(f"cantidad:{elemento['cantidad']}")
        print(f"fecha de inicio:{elemento['fecha inicio']}")
        print(f"fecha de devolucion:{elemento['fecha de devolucion']}")
        print("-"*20)





