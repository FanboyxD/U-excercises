class Mágico(object):
    def __init__(self):
        pass
    def cuadrado(self,matriz):
        if (isinstance(matriz,list))and len(matriz)==len(matriz[0]):
            return self.cu_aux(matriz,1)
        else:return "Error"
    def cu_aux(self,matriz,contador):
        if contador>(len(matriz)*len(matriz[0])):
            return True
        elif self.buscar(contador,matriz,0,0):
            return (self.cu_aux(matriz,contador+1))
        else:return False
    def buscar(self,elemento,matriz,fila,columna):
        if fila == len(matriz):
            return False
        elif columna==len(matriz[0]):
            return self.buscar(elemento,matriz,fila+1,0)
        elif elemento==matriz[fila][columna]:
            return True
        else: return self.buscar(elemento,matriz,fila,columna+1)
c=Mágico()
matriz=[[3,1,5],
        [4,7,2],
        [9,8,6]]
print(c.cuadrado(matriz))
