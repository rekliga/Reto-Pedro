class Problema:
    def __init__(self):
        self.primeros = list(range(1,101))

    def extract(self,numero=int()):
        try:
            self.primeros.remove(numero)
            #print(self.primeros)
        except ValueError:
            print("el numero ingresado no es un entero",numero)
            #1
    def calc(self):
        numero = set(range(1,101))-set(self.primeros)
        for i in numero:
            print(i)
            break
p = Problema()

p.extract(numero=3)
p.calc()

