from GestionarJson import cargar, crear,generar_id
from datetime import date
archivologs="Logs.json"

def Logmascantidad():
    logs=cargar(archivologs)
    
    
    
    
    
    
    Lista_logs={
        "id":generar_id(logs),
        "fecha":str(date.today()),
        "Detalle":"El usuario intentó solicitar más herramientas de las que hay disponibles"
            
        }
    logs.append(Lista_logs)
    crear(archivologs,logs)

def Logwrongusuario():
    logs=cargar(archivologs)
    
    
    
    
    
    
    Lista_logs={
        "id":generar_id(logs),
        "fecha":str(date.today()),
        "Detalle":"Un usuario no creado intentó solicitar una herramienta"
            
        }
    logs.append(Lista_logs)
    crear(archivologs,logs)

def lista_logs():
    logs=cargar(archivologs)
    for elemento in logs:
        print(f"ID:{elemento['id']}")
        print(f"fecha:{elemento['fecha']}")
        print(f"Detalle:{elemento['Detalle']}")
        print("-"*20)
