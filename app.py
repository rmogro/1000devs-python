from os import system
import time
from dal.db import Db
import bll.usuarios as user

def agregar():
    try:
        user_name = input("Ingrese el Usuario: ")
        if len(user_name) == 0 or user_name == None:        
            print("Usuario: valor requerido")
            return
        
        email = input("Ingrese el Email: ")
        if len(email) == 0 or email == None:        
            print("Email: valor requerido")
            return

        user.agregar(user_name, email)
        print("Registro agregado!")
    except Exception as ex:
        print("Se produjo un error en la aplicación:", ex)

def listar():
    result = user.listar()
    for data in result:
        print("""
        ID:        {}
        USUARIO:   {}
        EMAIL:     {}
        """.format(data[0], data[1], data[2]))

def actualizar():
    try:
        id = int(input("Ingresa el Id: "))
        if id > 0:
            user_name = input("Ingrese el Usuario: ")
            if len(user_name) == 0 or user_name == None:        
                print("Usuario: valor requerido")
                return
            
            email = input("Ingrese el Email: ")
            if len(email) == 0 or email == None:        
                print("Email: valor requerido")
                return
            
            user.actualizar(id, user_name, email)
            print("Registro actualizado!")
        else:
            print("Se require un Id válido")
    except Exception as ex:
        print("Se produjo un error en la aplicación:", ex)

def eliminar():
    try:
        id = int(input("Ingresa el Id: "))
        if id > 0:
            user.eliminar(id)
            print("Registro eliminado!")
        else:
            print("Se require un Id válido")
    except Exception as ex:
        print("Se produjo un error en la aplicación:", ex)

def filtrar():
    user_name = str(input("Buscar por Usuario: "))
    if len(user_name) > 0:
        result = user.filtrar(user_name)
        for data in result:
            print("""
            ID:        {}
            USUARIO:   {}
            EMAIL:     {}
            """.format(data[0], data[1], data[2]))
    else:
        print("Se require un Usuario para la busqueda")

def limpiarPantalla():
    system("cls")

def principal():
    Db.crear()    
    while True:        
        print("=========================================")
        print("\tProyecto Super")
        print("=========================================")
        print("\t[1] Listar usuarios")
        print("\t[2] Busqueda de usuarios")
        print("\t[3] Agregar usuario")
        print("\t[4] Modificar usuario")
        print("\t[5] Eliminar usuario")
        print("\t[6] Salir")
        print("=========================================")
        opcion = int(input("Seleccione una opción: "))

        try:            
            if opcion == 1:
                listar()
                time.sleep(1)                
            elif opcion == 2:
                filtrar()
                time.sleep(1)
            elif opcion == 3:
                agregar()
                time.sleep(1)
                limpiarPantalla()
            elif opcion == 4:
                actualizar()
                time.sleep(1)
                limpiarPantalla()
            elif opcion == 5:
                eliminar()
                time.sleep(1)
                limpiarPantalla()
            elif opcion == 6:
                break
            else:
                raise Exception("Opción incorrecta")
        except Exception as ex:            
            if str(ex) == "Opción incorrecta":
                print("Por favor, seleccione una opción válida")                
            else:
                print("Se produjo un error en la aplicación:", ex)

principal()
