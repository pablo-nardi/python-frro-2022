class Producto:
    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        
    def __str__(self):
        return """REFERENCIA\t{} \nNOMBRE\t\t{} \nPVP\t\t{} \nDESCRIPCIÓN\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion)


class Adorno(Producto):
    pass

a = Adorno(2034,"Vaso adornado",15,"Vaso de porcelana adornado con árboles")


print(a)