import math
from FiguraInicial import Fig
class Cuadrado(Fig):
    def __init__(self,x,y,lado):
        super().__init__(x,y)
        self.__lado = lado

    def getLado(self):
        return self.__lado

    def setLado(self,lado):
        self.__lado = lado

    def calcularaArea(self):
        return self.__lado*self.__lado

class Circulo(Fig):
    def __init__(self,x,y,r):
        super().__init__(x,y)
        self.__radio = r
    def getRadio(self,r):
        return self.__radio
    def setRadio(self,r):
        self.__radio = r
    def calcularArea(self):
        return math.pi*(self.__radio**2)
    
from CuadradoInicial import Cuadrado
class Rectangulo(Cuadrado):
    def __init__(self,x,y,lado,ancho):
        super().__init__(x,y,lado)
        self.__ancho = ancho

    def getAncho(self):
        return self.__ancho

    def setAncho(self,ancho):
        self.__ancho = ancho

    def calcularaArea(self):
        return super().getLado() * self.__ancho
