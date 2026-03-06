from Validaciones import ValidarMenu
from Submenus import MenuAdministrador, MenuUsuarios
from Funciones import Contraseña_correcta


contraseña_c=1243

def MenuPrincipal():
        while True:
                opmenuprincipal=ValidarMenu('''
                        Portal Prestamo de Herramientas
                                        
                Bienvenido, marque la opción segun su rol:

                                        
                1.Ingresar como usuario

                2.Ingresar como administrador (contraseña es 1243)
                                            
                3.Salir
                        
                ''' ,1,3)
                while opmenuprincipal==None:
                        opmenuprincipal=ValidarMenu('Intente nuevamente: ',1,3)

                match opmenuprincipal:
                        case 1: 
                                MenuUsuarios()
                        case 2:
                                confirma=Contraseña_correcta(contraseña_c)
                                while confirma==None:
                                        print("Contraseña incorrecta, intente nuevamente ")
                                        confirma=Contraseña_correcta(contraseña_c) 
                                MenuAdministrador()
                        case 3:
                                print("Gracias por usar nuestro servicio")
                                return
                        

                           