class Suma(object):
    def __init__(self):
        pass
    def Suma_matriz(self,m):
        if isinstance (m,list):
            return self.sumaM(m,0)/(len(m)*len(m[0]))
    def sumaM(self,m,resultado):
        if m==[]:
            return resultado
        elif isinstance(m[0],list):
            return self.sumaM(m[0],resultado)+self.sumaM(m[1:],resultado)
        else: return self.sumaM(m[1:],resultado+m[0])
s=Suma()
m=[[1,2,3],[4,5,6]]
print(s.Suma_matriz(m))
