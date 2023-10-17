import platform
import os
import json
from Python.ModuloCarrito import Carrito

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Darwin":
        cienofpy = print("Escribe los primeros 100 digitos de π o experimenta un shutdown:\n")
        if cienofpy == "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679":
           os.system("clear")
           print("Zafaste")
        else:
            os.system("sudo shutdown -h now")
    


def loadDB():
    try:
        with open("./usuarios.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

loadedDB = loadDB()

def saveDB(loadedDB):
    with open("./usuarios.json", "w") as file:
        json.dump(loadedDB, file)
    

class Cliente(Carrito):

    def __init__(self, userName=None, passWord=None, email=None):
        super().__init__()
        self.userName = userName
        self.passWord = passWord
        self.email = email
        self.clientID = 0 


    def showKart(self):
        clear()
        self.listado = loadedDB[self.userName]["carrito"]
        return super().showKart()
        
    
    def add2kart(self, producto):
        clear()
        super().add2kart(producto)
        loadedDB[self.userName]["carrito"]= self.listado
        saveDB(loadedDB)
        return
    
    def removeFromKart(self, producto):
        clear()
        super().removeFromKart(producto)
        loadedDB[self.userName]["carrito"] = self.listado
        saveDB(loadedDB)
        return

    def __str__(self):
        if self.clientID != 0:
            self.listado = loadedDB[self.userName]["carrito"]
            return f"Nombre de usuario: {self.userName} \nCorreo electrónico asociado: {self.email} \nID de cliente: {self.clientID} \nNúmero de objetos en el carrito: {len(self.listado)}"
        else:
            clear()
            return "Actualmente no hay ninguna sesión iniciada"

    def register(self, loadedDB):
        if len(loadedDB) >= 1:
            newClientID = len(loadedDB) + 1 
        else:
            newClientID = self.clientID + 1 
        
        if self.userName not in loadedDB or self.email not in loadedDB:
            loadedDB[self.userName] = {
                "user": self.userName,
                "passw": self.passWord,
                "email": self.email,
                "clientID": newClientID,
                "carrito": self.listado
            }
            clear()
            print("Usuario registrado exitosamente")
            saveDB(loadedDB)
            return
        elif self.userName in loadedDB:
            clear()
            print("El nombre de usuario ya ha sido utilizado")
            return
        elif self.email in loadedDB:
            clear()
            print("El email ya ha sido utilizado")
            return

    def login(self, loadedDB):
        if self.userName in loadedDB and self.passWord == loadedDB[self.userName]["passw"]:
            clear()
            print("Sesion iniciada exitosamente")
            self.userName = loadedDB[self.userName]["user"]
            self.email = loadedDB[self.userName]["email"]
            self.clientID = loadedDB[self.userName]["clientID"]
            self.listado = loadedDB[self.userName]["carrito"]
            print(f"Bienvenido a tu sesion {self.userName}")
            return 1 
        elif "@" in self.userName:
            for user, valoruser in loadedDB.items():
                if self.userName == valoruser["email"] and self.passWord == valoruser["passw"]:
                    self.userName = valoruser["user"]
                    self.email = valoruser["email"]
                    self.clientID = valoruser["clientID"]
                    self.listado = valoruser["carrito"]
                    clear()
                    print("Sesion iniciada exitosamente utilizando el mail")
                    print(f"Bienvenido a tu sesion {self.userName}")
                    return 1                 
        else:
            clear()
            print("Usuario o contraseña incorrectos")
            return 0 
    

        
    
#tasklist
#Programar Metodo Login DONETE
#Hacer que el login acepte email y username DONE
#Hacer el main EN PROCESO
#terminar rikrol 
#Testear todo 


