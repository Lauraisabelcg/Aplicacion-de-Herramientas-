#Problemas al prestar herramientas es:
#No hay control
#No se devuelven a tiempo
#Algunas se dañan
#No se sabe quien las tiene
#No hay registro de las disponibles

#Programa que registre las herramientas
#Programa que diga el estado de la herramienta
#puede ser activa, en reparacion, fuera de servicio
#Programa que registre los vecinos 
#Programa que registre los prestamos realizados
#Programa para consultar la informacion

#Herramientas debe de : Registrar id, nombre,
#categoria de la herramienta(jardineria, construccion)
#cantidad disponible,valor estimado
#valor estimado es a mi eleccion,
#cobrare por uso de herramienta?por perdida?por dias?
#por hora?por daño?

#Herramientas: menu: 1.Crear 2.Listar 3.Buscar
#4.Actualizar 5. Eliminar o inactivar(yo escojo si eli o inacti)
#Usuarios: Id, nombre, apellido, telefono, direccion
#tipo de usuario, residente o administrador
#Usuario: Puede consultar estado de herramientas(buen estado,dañoado/reparar),
#disponibilidad y quien la tiene/cuando estara dispo
# 
#el usuario debe poder pedir una herramienta y el admi
#debe de poder ver las solicitudes de herramientas
#"""Administrador""": crear, listar, buscar, actualizar,
#eliminar herramientas, eliminar usuario.
#solo el admi puede registrar a los usuarios y
#sus herramientas, para evitar suplantacion identidad
#GestionPrestamos: id del prestamo, usuario, herramienta
#cantidad,fecha de inicio,fecha de devolucion, estado 
#observaciones,condicionar maximo de prestamo

#Validar al prestar: disponibilidad, 
# luego ajustar el stock
#al devolver: ACtualizar el estado del prestamo (dispo)
#luego ajustar nuevamente el numero del stock dispo

#Consultar herramientas con bajo stock(menos 3 unidades)
#Prestamos activos(letrero de se le ha prestado x)
#y vencidos (letrero de debe devolver x) if = true:
#no se puede prestar otra herramienta
#Historial de prestamos de un usuario
#Herramientas + solicitadas
#Usuarios que + solicitan

#Registro de errores para admi 
# ejemplo: pedir mas unidades, intento de
#hackeo en la cuenta admin

