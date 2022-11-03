class Suma(object):
    def __init__(self):
        pass
    def Suma_matriz(self,m):
        if isinstance (m,list):
            return self.sumaM(m,0,0,0)
    def sumaM(self,m,f,c,resultado):
        if f==len(m):
            return resultado
        elif c==len(m[0]):
            return self.sumaM(m,f+1,0,resultado)
        else: return self.sumaM(m,f,c+1,resultado+m[f][c])
s=Suma()
m=[[1,2,3],[4,5,6]]
print(s.Suma_matriz(m))
