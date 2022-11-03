class Buscar(object):
    def __init__(self):
        pass
    def buscar_matriz(self,elemento,matriz):
        if isinstance(elemento,int)and (matriz,list):
            return self.bus_aux(elemento,matriz,0,0)
        else:return "Error"
    def bus_aux(self,elemento,matriz,fila,columna):
        if (fila == len(matriz)):
            return False
        elif (columna==len(matriz[0])):
            return self.bus_aux(elemento,matriz,fila+1,0)
        elif elemento==matriz[fila][columna]:
            return True
        else: return self.bus_aux(elemento,matriz,fila,columna+1)
b=Buscar()
matriz=[[1,2,3],[4,5,6]]
elemento=4
print(b.buscar_matriz(elemento,matriz))
