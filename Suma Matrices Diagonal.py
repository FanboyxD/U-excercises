class Suma(object):
    def __init__(self):
        pass
    def suma_matriz(self,matriz):
        if (isinstance(matriz,list)):
            return self.sum_aux(matriz,0,0,len(matriz)-1)
        else: return "Error"
    def sum_aux(self,matriz,resultado,f,c):
        if f==len(matriz):
            return resultado
        else: return self.sum_aux(matriz,resultado+matriz[f][c],f+1,c-1)
su=Suma()
matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]
print(su.suma_matriz(matriz))


def suma_matriz(matriz):
        if (isinstance(matriz,list)):
            return sum_aux(matriz,0,0,len(matriz)-1)
        else: return "Error"
def sum_aux(matriz,suma,f,largo):
        if f==len(matriz):
            return suma
        else: return sum_aux(matriz,suma+matriz[f][largo],f+1,largo-1)
matriz=[[6,6,6],
        [4,6,6],
        [2,7,6]]
print(suma_matriz(matriz))
