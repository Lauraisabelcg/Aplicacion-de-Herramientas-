from Validaciones import ValidarEntero

def Contraseña_correcta(contraseña_c):

        contraseña=ValidarEntero('Ingrese la contraseña: ')
        if contraseña==contraseña_c:
            print('Acceso concedido')
            return True
        else:
            return None


