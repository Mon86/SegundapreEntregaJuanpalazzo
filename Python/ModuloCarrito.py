class Carrito:
    def __init__(self):
        self.listado = []


    def add2kart(self, producto):
        self.listado.append(producto)
        print(f"{producto} fue agregado al carrito correctamente.")

    def removeFromKart(self, producto):
        try:
            self.listado.remove(producto)
            print(f"{producto} fue removido del carrito correctamente")
        except ValueError:
            print(f"{producto} no se encuentra en el carrito")

    def showKart(self):
       if self.listado != []:
         print(f"El carrito actualmente contiene:\n{self.listado}")
       else:
           print(f"El carrito actualmente esta vacio")

