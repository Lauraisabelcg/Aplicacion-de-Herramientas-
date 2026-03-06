from GestionarJson import cargar, crear 
from logs import Logmascantidad,Logwrongusuario

ARCHIVO_U="Usuarios.json"
ARCHIVO_HERRAMIENTAS="Herramientas.json"

def RestarHerramienta(nombre_herramienta):
    
    herramienta=cargar(ARCHIVO_HERRAMIENTAS)
    
    for elemento in herramienta:
        if nombre_herramienta.lower()==elemento["nombre"].lower():
            cantidad=int(input(f'Para solicitar una herramienta, ingrese la cantidad que necesita, actualmente cuenta con {elemento["cantidad"]} '))
            if cantidad>elemento["cantidad"]:
                Logmascantidad()
                print("no se puede prestar")
                return None
           
            else:
                elemento["cantidad"]-=cantidad
                
                print("solicitud exitosa!")
                crear(ARCHIVO_HERRAMIENTAS,herramienta)
            return cantidad
    print('no se ejecuto la accion')
    return None

def existeHerramienta(nombre):
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)
    for elemento in herramientas:
        if nombre.lower() == elemento["nombre"].lower():
            return True
    return False

def existenombreS(nombre):
    herramienta=cargar(ARCHIVO_U)
    for elemento in herramienta:
        if nombre.lower()==elemento["nombre"].lower():
            return True
    Logwrongusuario()
    return False