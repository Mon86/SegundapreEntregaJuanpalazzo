from Python.ModuloCliente import *
import sys 
import webbrowser

errorfatal = 0 

while True:
    print("Bienvenido a CoderGestionaTusCompras!")
    print("Presiona 1 para iniciar sesion")
    print("Presiona 2 para registrarte")
    print("Presiona 3 para salir")
    primerinput = input()
    if primerinput == "1":
        user = input("Ingresa tu nombre de usuario o tu email:\n")
        clear()
        passw = input("Ingresa tu contraseña:\n")
        sesion = Cliente(user,passw)
        sesion.login(loadedDB)
        if sesion.login(loadedDB) == True:
            while True:
                print("Presiona 1 para mostrar los contenidos de tu carrito")
                print("Presiona 2 para añadir un producto al carrito")
                print("Presiona 3 para remover un producto del carrito")
                print("Presiona 4 para cerrar sesion")
                segundoinput = input()
                if segundoinput == "1":
                    sesion.showKart()
                    continue
                elif segundoinput == "2":
                    tercerinput = input("Escribe el producto que quieras añadir al carrito:\n")
                    sesion.add2kart(tercerinput)
                    continue
                elif segundoinput == "3":
                    tercerinput = input("Escribe el producto que quieras remover del carrito:\n")
                    sesion.removeFromKart(tercerinput)
                elif segundoinput == "4":
                    clear()
                    print(f"Saliendo de la sesion\n"
                          f"Hasta la proxima {sesion.userName}")
                    break
                else:
                    print("Debes escoger una opcion valida")
                    continue
    elif primerinput == "2":
        user = input("Ingresa tu nombre de usuario:\n")
        clear()
        passw = input("Ingresa tu contraseña:\n")
        clear()
        email = input("Ingresa tu email:\n")
        sesion = Cliente(user,passw,email)
        sesion.register(loadedDB)
        continue
    elif primerinput == "3":
        sys.exit()
    else:
        clear()
        print("Debes escoger una opcion valida")
        errorfatal += 1 
        if errorfatal >= 5:
            webbrowser.open("bit.ly/3qhnzKG")
            continue

