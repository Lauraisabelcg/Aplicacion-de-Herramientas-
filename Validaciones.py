
def ValidarMenu(mensaje,minimo,maximo):
    try: 
        opmenu=int(input(mensaje))
        if opmenu<minimo or opmenu>maximo:
            print("Error,opcion no encontrada, escriba nuevamente ")
            return None
        else:
            return opmenu
    except: 
        return None
              
def ValidarEntero(mensaje):
    try:
        # 0  =   Ingrese el numero
        # 0  =    12
        # 12
        numero=int(input(mensaje))
        return numero
    except:
        return None
def ValidarEnteroyNega(mensaje,minimo):
    try: 
        numero=int(input(mensaje))
        if numero<minimo:
            print("No se aceptan numero negativos ni letras ")
            return None
        else:
            return numero
    except: 
        return None
    
def Validarn_herramientas(mensaje,minimo):
    try: 
        n_herramienta=int(input(mensaje))
        if n_herramienta<minimo:
            print("Error,opcion no encontrada, escriba nuevamente ")
            return None
        else:
            return n_herramienta
    except: 
        return None
    
def nombrevalido(nombre):
    if nombre.strip()=="":
        return False
    return True

def Validarn_Telefono(mensaje,minimo,maximo):
    try: 
        n_telefono=int(input(mensaje))
        if n_telefono<minimo or n_telefono>maximo:
            print("Error, el numero de telefono debe tener 10 numeros")
            return None
        else:
            return n_telefono
    except: 
        return None
    
def Validar_cantidad_he(mensaje,minimo,maximo):
    try: 
        cantidad_he=int(input(mensaje))
        if cantidad_he<minimo or cantidad_he>maximo:
            print("Error, no hay disponibilidad")
            return None
        else:
            return cantidad_he
    except: 
        return None