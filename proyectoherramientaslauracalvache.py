
from Validaciones import ValidarMenu
from GestionarHerramientas import agregar_herramienta, lista_herramientas, actualizar_H, eliminar_herramienta, agregarHerramientaActual
from GestionarUsuarios import agregar_usuarios, lista_usuarioss, actualizar_U, eliminar_usuarios
from GestionarSolicitudes import Solicitar_Herramienta, lista_solicitud


def MenuAdministrador():
    opmenuadmi=ValidarMenu('''
              Hola Administrador,¿Que desea hacer hoy?

            1. Manejo herramientas
                           
            2. Manejo Usuarios
                           
            3.Consultar historial de prestamos de usuarios

                           ''',1,3)
    
    while opmenuadmi==None:
        opmenuadmi=ValidarMenu('',1,3)
    match opmenuadmi:
        case 1:
            Submenu_Herramientas()
        case 2:
            Submenu_Usuarios()
        case 3:
            lista_solicitud()

def Submenu_Herramientas():
    while True:
        sub_H_op=ValidarMenu('''
                MENU HERRAMIENTAS
                             
                1.Agregar una nueva herramienta
                             
                2.Consultar Lista de las Herramientas
                             
                3.Actualizar nombre de la Herramienta
                             
                4.Eliminar una Herramienta del registro
                             
                5.Agregar mas cantidades de un mismo tipo de Herramienta
                             
                6.Regresar al Menu Administrador
                             
                             
                            
                            ''',1,6)
        while sub_H_op==None:
            sub_H_op=ValidarMenu('',1,6)
        match sub_H_op:
            case 1:
                agregar_herramienta()
            case 2:
                lista_herramientas()
            case 3:
                actualizar_H()
            case 4:
                eliminar_herramienta()
            case 5:
                lista_herramientas()
                agregar_herramienta()         
            case 6:
                MenuAdministrador()

def Submenu_Usuarios():
    while True:
        sub_H_op=ValidarMenu('''
                MENU USUARIOS
                             
                1.Agregar un nuevo usuario
                             
                2.Consultar Lista de los usuarios actuales
                             
                3.Actualizar datos del usuario                                                               
                             
                4.Eliminar un Usuario del registro
                             
                5.Regresar al Menu Administrador
                             
    
                            
                            ''',1,5)
        while sub_H_op==None:
            sub_H_op=ValidarMenu('',1,5)
        match sub_H_op:
            case 1:
                agregar_usuarios()
            case 2:
                lista_usuarioss()
            case 3:
                actualizar_U()
            case 4:
                eliminar_usuarios()
            case 5:
                MenuAdministrador()

def MenuUsuarios():
    while True:
        opmenu_Usuario=ValidarMenu('''
              Bienvenido, ¿Que desea hacer hoy?

            1. Ver lista de herramientas
                           
            2. Quiero usar una Herramienta
                           
            3. Consultar historial de prestamos de usuarios
                           
            4. Salir
                           ''',1,4)
    
        while opmenu_Usuario==None:
            opmenu_Usuario=ValidarMenu('',1,4)
        match opmenu_Usuario:
            case 1:
                lista_herramientas()
            case 2:
                Solicitar_Herramienta()
            case 3:
                lista_solicitud()
            case 4:
                print("Gracias por usar nuestro servicio")
                break