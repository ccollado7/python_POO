#Metodos

class Matematica:
    def suma(self):
        self.n1 = 2
        self.n2 = 3
        return self.n1 + self.n2

s = Matematica()
s.suma()
print(s.n1 + s.n2)
print(s.suma())


class Ropa:
    def __init__(self):
        self.marca = "Lacoste"
        self.talle = "L"
        self.color = "Rojo"

prenda = Ropa()
print(prenda.marca)
print(prenda.talle)
print(prenda.color)

class Ropa_1:
    def __init__(self,marca,talle,color):
        self.marca = marca
        self.talle = talle
        self.color = color

prenda_1 = Ropa_1("kevingston","S","Rojo")
print(prenda_1.marca)
print(prenda_1.talle)
print(prenda_1.color)


class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2

operacion = Calculadora(10,2)
print(operacion.producto)
