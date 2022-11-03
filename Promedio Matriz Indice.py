class Sumatriz(object):
    def __init__(self):
        pass
    def sumar(self,matriz):
        if isinstance (matriz,list):
            return self.sum_aux(matriz,0,0)/len(matriz)
        else:return "Error"
    def sum_aux(self,matriz,fila,resultado):
        if fila == len(matriz):
            return resultado 
        elif (isinstance(matriz[fila],list)):
            return (self.fila_aux(matriz[fila],0,resultado)
                    +self.sum_aux(matriz,fila+1,resultado))
    def fila_aux(self,fila,col,resultado):
        if (col==len(fila)):
            return resultado/col
        else:return self.fila_aux(fila,col+1,resultado+fila[col])

s=Sumatriz()
matriz=[[1,2,3,4],[5,6,7,8]]
print(s.sumar(matriz))
