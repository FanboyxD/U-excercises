class Sumatriz(object):
    def __init__(self):
        pass
    def sumar(self,matriz):
        if isinstance (matriz,list):
            return self.sum_aux(matriz,0,0,[])
        else:return "Error"
    def sum_aux(self,matriz,c,f,resultado):
        if f == len(matriz):
            return resultado
        elif c==len(matriz[0])-1:
            return (self.sum_aux(matriz,0,f+1,resultado))
        elif(isinstance(matriz[f][c],int)and matriz[f][c]<matriz[f-1][c-1]):
            return (self.sum_aux(matriz,c+1,f,resultado+[[f]+[c]]))
        else:
            return self.sum_aux(matriz,c+1,f,resultado)

s=Sumatriz()
matriz=[[1,2,3],[4,3,6]]
print(s.sumar(matriz))
